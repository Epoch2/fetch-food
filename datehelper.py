# -*- coding: utf-8 -*-
import re
import datetime

weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def weekday_to_weeknumber(string, currentday):
    day_of_week = -1
    for day in weekdays:
        day_of_week += 1
        if day in string:
            return day_of_week
    return currentday

def to_string(date):
    return date.strftime("%Y-%m-%d")

def current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d\r%H:%M:%S")

def weekday_to_date(init_date, day_of_week):
    date = init_date + datetime.timedelta(days=day_of_week)
    return date

def find_date(string):
    REGEX_DATE = r"^\d{4}\.\d{2}\.\d{1,2}"  #matches dddd.dd.d(d) where d is digit 0-9
    date_split = re.match(REGEX_DATE, string).group().split(".")
    date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
    return date

def is_weekday(string):
    REGEX_WEEKDAY = u"^(Måndag|Tisdag|Onsdag|Torsdag|Fredag)"
    if re.match(REGEX_WEEKDAY, string) is not None:
        return True
    else:
        return False
