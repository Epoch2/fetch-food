import config
from bs4 import BeautifulSoup

class PropertyParser(object):

    selectable_date_identifier = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_ctl01 select[name=ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek] option"
    content_identifier = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_MenuUpdatePanel div[class=ContentArea] p"
    property_identifier = "input"

    def __init__(self, page):
        self.page_soup = BeautifulSoup(page)

    def reinit(self, page):
        print "REINIT"
        self.page_soup = BeautifulSoup(page)

    def get_selectable_dates(self):
        date_soup = self.page_soup.select(PropertyParser.selectable_date_identifier)
        datelist = []

        for optiontag in date_soup:
            datelist.append(optiontag["value"])
        return datelist

    def get_entry_list(self):
        content_soup = self.page_soup.select(PropertyParser.content_identifier)
        entrylist = []

        for entry in content_soup:
            entrylist.append(entry.contents[0].strip())
        return entrylist

    def get_properties(self):
        property_soup = self.page_soup.select(PropertyParser.property_identifier)
        properties =  {}

        for propertytag in property_soup:
            print propertytag
            if propertytag["name"][0] == "_" and propertytag["name"][1] == "_":
                properties[propertytag["name"]] = propertytag["value"]
        return properties
