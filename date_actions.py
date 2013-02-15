weekdays = [u"Måndag", u"Tisdag", u"Onsdag", u"Torsdag", u"Fredag"]

def is_weekday(string):
    for day in weekdays:
        if day in string:
            return True
        else:
            return False
