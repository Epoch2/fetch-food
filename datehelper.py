weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def is_weekday(string):
    day_of_week = -1
    for day in weekdays:
        day_of_week += 1
        if day in string:
            return day_of_week

    return False

def getDateFromDay(init_date, day):
    dateSoup = html.select(dateSelectString)
    plainText = dateSoup[0].contents[0].strip()
    dateSplit = re.match(REGEX_DATE, plainText).group().split(".")

    initialDate = datetime.date(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
    requestedDate = initialDate + datetime.timedelta(days=dayOfWeek)
    requestedDate_s = requestedDate.strftime("%Y-%m-%d")

    return requestedDate_s
