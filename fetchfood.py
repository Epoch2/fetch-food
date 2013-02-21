#!/usr/bin/python
# -*- coding: utf-8 -*-

# FetchFood
# Fetch menu data from page, structurize it and POST it to webserver.

import urllib2
import re
import time
import sys
import http
import parse
import datehelper
import food
import mail
import error
import config
import passwd
from bs4 import BeautifulSoup

def generate_food_entries(url, suburl):
    entrylist = []
    for date in parse.get_selectable_dates(http.get_page_from_url(url + suburl)):
        headers = config.POST_DEFAULT_HEADERS
        data = {config.AMICA_TYPE_KEY : "Lunch",
                config.AMICA_WEEK_KEY : date}
        page = http.post_data(url, suburl, headers, data)
        page_soup = BeautifulSoup(page)
        content_soup = page_soup.select(config.TARGET_CONTENT_IDENTIFIER)

        food_generator = food.FoodEntryGenerator(datehelper.to_date(date))
        entrylist_special = []

        for p_tag in content_soup:
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

def post_entries(entrylist):
    entrycount = 0
    for entry in entrylist:
        postdata = entry.get_data();
        try:
            post.post_portaln(config.ACTION_POST_FOOD, postdata)
            entrycount += 1
        except http.HTTPException:
            raise
    return entrycount

def round_time(time):
    return str(round(time, 4))

#####

errorhandler = error.ErrorHandler()
entrylist = generate_food_entries(config.TARGET_URL, config.TARGET_SUBURL)

try:
    post.post_portaln(config.ACTION_CLEAR_TABLE) #Clear database table.
except http.HTTPException as e:
    errorhandler.add_error(e, config.ERROR_CLEAR_TABLE_FATAL)
entrycount = 0
try:
    entrycount = post_entries(entrylist)
except http.HTTPException as e:
    errorhandler.add_error(e, config.ERROR_POST_ENTRY_FATAL)

nl = config.CONFIG_MAIL_NEWLINE
mail_content = ("fetchfood.py completed at:" + nl + nl + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + nl + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + nl + nl + "Entries posted: " + str(entrycount))

if errorhandler.has_error:
    mail_content += nl + nl + "These (non-fatal) errors occurred during execution:" + nl + errorhandler.get_errors_compiled()

if config.CONFIG_MAIL_ENABLED:
    mail.sendmail("FetchFood Completed!", mail_content)
sys.exit(0)
