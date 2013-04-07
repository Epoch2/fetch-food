#!/usr/bin/python
# -*- coding: utf-8 -*-

# FetchFood
# Fetch menu data from page, structurize it and POST it to webserver.

import urllib
import re
import sys
import time
import http
import parse
import datehelper
import food
import mail
import error
import config

def clear_duplicates(_list):
    for item in _list:
        duplicates = 0
        for compare_item in _list:
            if item == compare_item:
                duplicates += 1
        if duplicates >= 2:
            duplicates -= 1
            for i in xrange(duplicates):
                _list.remove(item)

    return _list

def a_generate_food_entries(url):
    entrylist = []
    page_cache = ""
    init_page = http.get_page_from_url(url)
    parser = parse.PropertyParser(init_page)
    for date in parser.get_selectable_dates():
        headers = config.POST_DEFAULT_HEADERS
        headers.update(config.AMICA_HEADERS)
        data = {config.AMICA_TYPE_KEY : "Lunch",
                config.AMICA_WEEK_KEY : date}
        data.update(parser.get_properties())
        data.update(config.AMICA_POST_DATA)
        try:
            page = http.post_data(url, headers, data)
        except http.HTTPException:
            raise
        parser.reinit(page)
        if page in page_cache:
            print "same shit"
        else:
            print "different shit"
            page_cache = page

        food_generator = food.FoodEntryGenerator(datehelper.to_date(date))
        entrylist_special = []

        for entry_plaintext in parser.get_entry_list():
            entry = food_generator.generate_entry(entry_plaintext)

            if entry is not None:
                if entry.hasinfo:
                    entrylist_special.append(entry)
                else:
                    entrylist.append(entry)

        for entry in entrylist_special:
            entry.info = food_generator.generated_info
            entrylist.append(entry)

    return clear_duplicates(entrylist)

def generate_food_entries(url):
    entrylist = []
    page_cache = ""
    init_page = http.get_page_from_url(url)
    parser = parse.PropertyParser(init_page)

    date = parser.get_selectable_dates()[0]

    food_generator = food.FoodEntryGenerator(datehelper.to_date(date))
    entrylist_special = []

    for entry_plaintext in parser.get_entry_list():
        entry = food_generator.generate_entry(entry_plaintext)

        if entry is not None:
            if entry.hasinfo:
                entrylist_special.append(entry)
            else:
                entrylist.append(entry)

    for entry in entrylist_special:
        entry.info = food_generator.generated_info
        entrylist.append(entry)

    return clear_duplicates(entrylist)

def post_entries(url, entrylist):
    entrycount = 0
    for entry in entrylist:
        postdata = entry.get_data()
        try:
            http.post_portaln(url, config.PORTALN_ACTION["post_food"], postdata)
            entrycount += 1
        except http.HTTPException as e:
            raise
    return entrycount

#####

def main():
    start_time = time.time()
    errorhandler = error.ErrorHandler()
    try:
        entrylist = generate_food_entries(config.TARGET_URL)
    except http.HTTPException as e:
        errorhandler.add_error(e, config.ERROR_FATAL["postback"])

    entrycount = 0
    for url in config.PORTALN_POST_URLS:
        try:
            http.post_portaln(url, config.PORTALN_ACTION["clear_table"]) #Clear database table.
        except http.HTTPException as e:
            errorhandler.add_error(e, config.ERROR_FATAL["clear_table"])
        try:
            entrycount = post_entries(url, entrylist)
        except http.HTTPException as e:
            errorhandler.add_error(e, config.ERROR_FATAL["post_entry"])

    total_time = time.time() - start_time

    nl = config.CONFIG["mail_newline"]
    mail_content = ("fetchfood.py completed at:" + nl + nl +
    datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + nl +
    datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + nl + nl +
    "Entries posted: " + str(entrycount) + nl +
    "Execution time: %.1fs") % total_time

    if errorhandler.has_error:
        print("error")
        mail_content += nl + nl + "These (non-fatal) errors occurred during execution:" + nl + errorhandler.get_errors_compiled()

    if config.CONFIG["mail_enabled"]:
        mail.sendmail("FetchFood Completed!", mail_content)
    elif config.DEBUG:
        print(mail_content)
    sys.exit(0)

if __name__ == "__main__":
    main()
