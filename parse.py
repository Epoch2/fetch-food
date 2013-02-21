import config
from bs4 import BeautifulSoup

class PropertyParser(object):

    selectable_date_identifier = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_ctl01 select[name=ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek] option"
    content_identifier = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_MenuUpdatePanel div[class-=ContentArea] p"
    viewstate_identifier = "input[name=__VIEWSTATE]"

    def __init__(self, page):
        self.page_soup = BeautifulSoup(page)

    def reinit(page):
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

    def get_viewstate(self):
        viewstatetag = self.page_soup.select(PropertyParser.viewstate_identifier)
        return viewstatetag[0]["value"]

