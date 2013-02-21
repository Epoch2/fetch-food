# -*- coding: utf-8 -*-
import re
import datetime

PRECISION_DATE = "%Y-%m-%d" #2013-05-05
PRECISION_TIME = "%H:%M:%S" #13:20:22
WEEKDAYS = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def weekday_to_weekdaynumber(string, currentday):
    day_of_week = -1
    for day in WEEKDAYS:
        day_of_week += 1
        if day in string:
            return day_of_week
    return currentday

def to_string(date, precision=PRECISION_DATE):
    return date.strftime(precision)

def current_date():
    return datetime.datetime.now()

def weekday_to_date(init_date, day_of_week):
    date = init_date + datetime.timedelta(days=day_of_week)
    return date

def to_date(string):
    REGEX_DATE = r"^\d{4}[\.-_]\d{2}[\.-_]\d{1,2}"  #matches YYYY.MM.DD, YYYY-MM-DD, YYYY_MM_DD
    REGEX_SEPARATORS = r"[\.-_]+"
    date_split = re.findall(REGEX_SEPARATORS, re.match(REGEX_DATE, string))
    #date_split = re.match(REGEX_DATE, string).group().split(".")
    date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
    return date

def is_weekday(string):
    REGEX_WEEKDAY = u"^(Måndag|Tisdag|Onsdag|Torsdag|Fredag)"
    if re.match(REGEX_WEEKDAY, string) is not None:
        return True
    else:
        return False
