#!/usr/bin/python
# -*- coding: utf-8 -*-

# FetchFood
# Fetch menu data from page, structurize it and POST it to webserver.

import urllib2
import re
import time
import sys
import datehelper
import food
import post
import mail
import error
import config
import passwd
from bs4 import BeautifulSoup

def generate_food_entries(date, soup):
    entrylist = []
    entrylist_special = []
    food_generator = food.FoodEntryGenerator(date)

    for p_tag in soup:
        plaintext = p_tag.contents[0].strip() #html -> plaintext
        entry = food_generator.generate_entry(plaintext)

        if entry is not None:
            if entry.hasinfo:
                entrylist_special.append(entry)
            else:
                entrylist.append(entry)

    for entry in entrylist_special:
        entry.info = food_generator.generated_info
        entrylist.append(entry)
    return entrylist

def round_time(time):
    return str(round(time, 4))

#####

exec_timekeys = ["total", "target_request", "generate_entries", "clear_table", "post_entry_all"]
exec_timekeys_description = ["Total execution time", "Time getting menu", "Time generating entries", "Time clearing DB", "Time posting to DB"]
exec_times = [0]*5
exec_times[0] = time.clock()
exec_times[1] = time.clock()
errorhandler = error.ErrorHandler()

try:
    page = urllib2.urlopen(config.TARGET_URL)
except urllib2.HTTPError as e:
    errorhandler.add_error(e, True)
except urllib2.URLError as e:
    errorhandler.add_error(e, True)
exec_times[1] = time.clock() - exec_times[1]

page_soup = BeautifulSoup(page)
page.close()
date_soup = page_soup.select("h2#" + config.DATE_INNER_ID)
date_plaintext = date_soup[0].contents[0].strip()
date = datehelper.find_date(date_plaintext)
content_soup = page_soup.select("div#" + config.CONTENT_OUTER_ID +
                                " div[class-=" + config.CONTENT_INNER_CLASS +
                                "] p")
exec_times[2] = time.clock()
entrylist = generate_food_entries(date, content_soup)
exec_times[2] = time.clock() - exec_times[2]
exec_times[3] = time.clock()
try:
    post.post(config.ACTION_CLEAR_TABLE) #Clear database table.
except post.PostException as e:
    errorhandler.add_error(e, True)
exec_times[3] = time.clock() - exec_times[3]
exec_times[4] = time.clock()
try:
    entrycount = post.post_entries(entrylist)
except post.PostException as e:
    errorhandler.add_error(e, True)

exec_times[4] = time.clock() - exec_times[4]
exec_times[0] = time.clock() - exec_times[0]

for i, time in enumerate(exec_times):
    postdata = {exec_timekeys[i] : time}
    try:
        post.post(config.ACTION_POST_INFO, postdata)
    except post.PostException as e:
        errorhandler.add_error(e, False)

mail_content = "fetchfood.py completed at:\n\n" + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + "\n" + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + "\n\nEntries posted: " + str(entrycount)
exec_times_string_list = [mail_content]
for i, t in enumerate(exec_times):
    exec_times_string_list.append("\n    " + exec_timekeys_description[i] + ": " + round_time(t))
mail_content = "".join(exec_times_string_list)

if config.CONFIG_MAIL_ENABLED:
    mail.sendmail("FetchFood Completed!", mail_content)
sys.exit(0)
