import datecheck

class FoodEntry:

    def __init__(self, date, type_, content, hasinfo=False, info=""):
        self.date = date
        self.type_ = type_
        self.content = content
        self.hasinfo = hasinfo
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

class FoodEntryGenerator:

    def __init__(self, init_date):
        self.date = init_date
        self.weekday_index = 0

    def increase_day(self, amount):


    def generate_entry(string):
        if datehelper.is_weekday(string):
            self.date = datehelper.get_date_from_day
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

            return
