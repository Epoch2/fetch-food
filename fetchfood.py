#!/usr/bin/python
# -*- coding: utf-8 -*-

# FetchFood
# Fetch menu data from page, structurize it and POST it to webserver.

import urllib
import urllib2
import httplib
import re
import datetime
import time
import sys
import os
import config
from bs4 import BeautifulSoup

class FoodEntry:

    def __init__(self, date, type_, content, info=""):
        self.date = date
        self.type_ = type_
        self.content = content
        self.info = info

    def compareTo(self, cprObject):
        if (self.date == cprObject.date and
            self.type_ == cprObject.type_ and
            self.content == cprObject.content and
            self.info == cprObject.info):
            return True
        else:
            return False

    def getData(self):
        return {"date" : self.date.encode("utf-8"),
                "type" : self.type_.encode("utf-8"),
                "content" : self.content.encode("utf-8"),
                "info" : self.info.encode("utf-8")}

class FoodEntryException(Exception):

    def __init__(self, exception):
        self.exception = exception

def getDateFromDay(html, dayOfWeek):
    REGEX_DATE = r"^\d{4}\.\d{2}\.\d{1,2}"  #matches dddd.dd.d(d) where d is digit 0-9
    dateSelectString = "h2#" + config.DATE_INNER_ID

    dateSoup = html.select(dateSelectString)
    plainText = dateSoup[0].contents[0].strip()
    dateSplit = re.match(REGEX_DATE, plainText).group().split(".")

    initialDate = datetime.date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
    requestedDate = initialDate + datetime.timedelta(days=dayOfWeek)
    requestedDate_s = requestedDate.strftime("%Y-%m-%d")

    return requestedDate_s

def getDateTypeContent(html, outerId, innerClass):
    REGEX_TYPE = r".+?(?=\s*[A-ZÅÄÖ])"      #matches Lunch, Soppa, etc
    REGEX_WEEK = r"v\.\d{1,2}$"             #matches v.3, v.24, etc
    REGEX_INFO = r"^\*=.+$"                 #matches *=innehåller fläskött, etc
    REGEX_GOODMEAL = r"^Smaklig.*"          #matches Smaklig Måltid
    REGEX_WHITESPACE = r"^$"                #matches ""

    DEFAULT_TYPE = "Mat"
    UNKNOWN_TYPE = "UNKNOWN_TYPE"

    weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]
    dayContent = [[]*5 for x in xrange(5)]  #5*5 array
    entryList = []
    specialList = []
    dayIndex = -1
    matchedWeek = False
    selectString = "div#" + outerId + " div[class-=" + innerClass + "] p"
    contentSoup = html.select(selectString)

    for pTag in contentSoup:
        plainText = pTag.contents[0].strip() #html -> plaintext
        matchedWeek = False
        for day in weekdays:
            if day in plainText: #if current row displays dayofweek
                dayIndex += 1
                weekdays.pop(0)
                matchedWeek = True
                break
        if (matchedWeek):
            continue

        date = getDateFromDay(html, dayIndex)

        if (not re.match(REGEX_WEEK, plainText)
            and not re.match(REGEX_GOODMEAL, plainText)
            and not re.match(REGEX_WHITESPACE, plainText)
            and not re.match(REGEX_INFO, plainText)): #if row isn't dayofweek, weeknumber, type, empty, goodmeal, or info, then create entry
            #date = getDateFromDay(html, dayIndex)
            typeObject = re.match(REGEX_TYPE, plainText)

            if typeObject is not None:
                try:
                    type_ = typeObject.group().strip()
                except AttributeError:
                    type_ = UNKNOWN_TYPE
            else:
                type_ = DEFAULT_TYPE

            content = plainText.replace(type_, "").strip()

            if "*" in content:
                specialList.append(FoodEntry(date, type_, content.replace("*", "")))
            else:
                entryList.append(FoodEntry(date, type_, content))

        elif re.match(REGEX_INFO, plainText):
            info = re.match(REGEX_INFO, plainText).group().replace("*=", "").strip()
            for entry in specialList:
                entry.info == info

        elif (not re.match(REGEX_INFO, plainText)
            and not re.match(REGEX_WHITESPACE, plainText)):
            type_ = DEFAULT_TYPE
            content = plainText.replace(type_, "").replace("*", "").strip()
            entryList.append(FoodEntry(date, type_, content))

    if (len(weekdays) > 0):
        raise FoodEntryException("Days missing from menu.")

    for entry in specialList:
        entryList.append(entry)

    return entryList

def post(url, page, headers, action, data={}):
    data['action'] = action
    data_encoded = urllib.urlencode(data)
    connection = httplib.HTTPConnection(url)

    try:
        connection.request("POST", page, data_encoded, headers)
    except httplib.HTTPException as e:
        mailInfo("FetchFood ERROR!", "Error requesting POST to " + url + page + " ->\rHTTPError")
        connection.close()
        sys.exit(1)
    response = connection.getresponse()
    responseData = response.read()

    return True

def clearTable(url, page, passwd):
    passwd_structured = {"passwd" : passwd}
    passwd_encoded = urllib.urlencode(passwd_structured)
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    connection = httplib.HTTPConnection(url)

    try:
        connection.request("POST", page, passwd_encoded, headers)
    except httplib.HTTPException as e:
        mailInfo("FetchFood ERROR!", "Error clearing table by requesting post to " + url + page + " -> \rHTTPError")
        connection.close()
        sys.exit(1)
    response = connection.getresponse()
    responseData = response.read()


def mailInfo(subject, content):
     os.system(("sendemail -q -f " + config.EMAIL_FROM + " -t " + config.EMAIL_TO + " -s " + config.EMAIL_SERVER + " -xu " + config.EMAIL_USER + " -xp " + passwd.EMAIL_PASSWD + " -u " + subject + " -m " + content))



#############



initTime = time.time()

try:
    page = urllib2.urlopen(config.TARGET_URL)
except urllib2.URLError as e:
    mailInfo("FetchFood ERROR!", "Error requesting GET to " + config.TARGET_URL + " ->\r" + str(e.reason))
    sys.exit(1)
except urllib2.HTTPError as e:
    mailInfo("FetchFood ERROR!", "Error requesting GET to " + config.TARGET_URL + " ->\r" + str(e.code) + ", " + str(e.reason))
    sys.exit(1)
pageSoup = BeautifulSoup(page)
page.close()
foodEntries = getDateTypeContent(pageSoup, config.CONTENT_OUTER_ID, config.CONTENT_INNER_CLASS)
post(config.POST_URL, config.POST_PAGE, config.POST_HEADERS, config.ACTION_CLEAR_TABLE)

entryCount = 0
for entry in foodEntries:
    postData = entry.getData();
    try:
        post(config.POST_URL, config.POST_PAGE, config.POST_HEADERS, config.ACTION_POST_FOOD, postData)
    except FoodEntryException as e:
        mailInfo("FetchFood ERROR!", "Error generating entries ->\r" + str(e.exception))
        sys.exit(1)
    else:
        entryCount += 1

endTime = time.time()
executionTime = endTime - initTime
mailContent = "fetchfood.py successfully ran at:\r\r" + datetime.datetime.now().strftime("%Y-%m-%d\r%H:%M:%S") + "\r\rEntries posted: " + str(entryCount) + "\rExecution time: " + str(round(executionTime, 2)) + "s"
mailInfo("FetchFood Completed!", mailContent)
sys.exit(0)

