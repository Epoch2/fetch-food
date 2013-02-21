from bs4 import BeautifulSoup

def get_selectable_dates(page):
    page_soup = BeautifulSoup(page)
    date_soup = page_soup.select(config.TARGET_SELECTABLE_DATE_IDENTIFIER)
    datelist = []

    for optiontag in date_soup:
        datelist.append(optiontag["value"])

    return datelist
