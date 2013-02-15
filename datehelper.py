import datetime

weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def is_weekday(string):
    day_of_week = -1
    for day in weekdays:
        day_of_week += 1
        if day in string:
            return day_of_week

    return None

def date_from_weekday(init_date, day_of_week):
    requested_date = init_date + datetime.timedelta(days=day_of_week)
    requested_date = requested_date.strftime("%Y-%m-%d")

    return requested_date
