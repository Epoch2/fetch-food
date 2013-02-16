import datetime

weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def is_weekday(string, currentday):
    day_of_week = -1
    for day in weekdays:
        day_of_week += 1
        if day in string:
            return True

    return currentday

def current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d\r%H:%M:%S")

def weekday_to_date(init_date, day_of_week):
    date = init_date + datetime.timedelta(days=day_of_week)
    date = requested_date.strftime("%Y-%m-%d")

    return date

def find_date(string):
    REGEX_DATE = r"^\d{4}\.\d{2}\.\d{1,2}"  #matches dddd.dd.d(d) where d is digit 0-9
    date_split = re.match(REGEX_DATE, plaintext).group().split(".")
    date = datetime.date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))

    return date
