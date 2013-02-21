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
    page_cache = ""
    init_page = http.get_page_from_url(url + suburl)
    parser = parse.PropertyParser(init_page)
    for date in parser.get_selectable_dates():
        headers = config.POST_DEFAULT_HEADERS
        data = {config.AMICA_TYPE_KEY : "Lunch",
                config.AMICA_WEEK_KEY : date,
                "__VIEWSTATE" : parser.get_viewstate()}
        print parser.get_viewstate()
        #data.update(config.AMICA_POST_DATA)
        try:
            page = http.post_data(url, suburl, headers, data)
        except http.HTTPException as e:
            raise
        parser.reinit(page)
        if page in page_cache:
            print "same shit"
        else:
            print "different shit"
            page_cache = page

        food_generator = food.FoodEntryGenerator(datehelper.to_date(date))
        entrylist_special = []

        for entry in parser.get_entry_list():
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
            post.post_portaln(config.PORTALN_ACTION["post_food"], postdata)
            entrycount += 1
        except http.HTTPException:
            raise
    return entrycount

def round_time(time):
    return str(round(time, 4))

#####

def main():
    errorhandler = error.ErrorHandler()
    try:
        entrylist = generate_food_entries(config.TARGET_URL, config.TARGET_SUBURL)
    except http.HTTPException as e:
        print str(e)

    try:
        http.post_portaln(config.PORTALN_ACTION["clear_table"]) #Clear database table.
    except http.HTTPException as e:
        errorhandler.add_error(e, config.ERROR_FATAL["clear_table"])
    entrycount = 0
    try:
        entrycount = post_entries(entrylist)
    except http.HTTPException as e:
        errorhandler.add_error(e, config.ERROR_FATAL["post_entry"])

    nl = config.CONFIG["mail_newline"]
    mail_content = ("fetchfood.py completed at:" + nl + nl + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + nl + datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + nl + nl + "Entries posted: " + str(entrycount))

    if errorhandler.has_error:
        mail_content += nl + nl + "These (non-fatal) errors occurred during execution:" + nl + errorhandler.get_errors_compiled()

    if config.CONFIG["mail_enabled"]:
        mail.sendmail("FetchFood Completed!", mail_content)
    sys.exit(0)

if __name__ == "__main__":
    main()
