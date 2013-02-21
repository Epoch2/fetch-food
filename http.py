import urllib2
import urllib
import httplib
import mail
import config
import passwd
from bs4 import BeautifulSoup

class HTTPException(Exception):

    def __init__(self, type_, exception, url):
        self.type_ = type_
        self.exception = exception
        self.url = url

    def __str__(self):
        return self.type_ + ": " + self.exception + " -> " + self.url

def get_page_from_url(url):
    try:
        page = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        raise GETError("GET", e, url)
    except urllib2.URLError as e:
        raise GETError("GET", e, url)
    else:
        page_content = page.read()
        return page_content

def post_data(url, page, headers, data):
    data_encoded = urllib.urlencode(data)
    request = urllib2.Request(url, data_encoded, headers)
    try:
        page = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        raise HTTPException("POST", e, url)
    except urllib2.URLError as e:
        raise HTTPException("POST", e, url)
    else:
        page_content = page.read()
        page.close()
        return page_content

def post_portaln(action, data={}):
    data["action"] = action
    data["passwd"] = passwd.POST_PASSWD
    response = post_data(config.POST_URL, config.POST_SUBURL, config.POST_DEFAULT_HEADERS, data)
    response = response.replace("\n", "").strip()

    try:
        response_code = int(response[0] + response[1])
    except ValueError:
        raise HTTPException("PORTALN.SE", "Internal server error", config.POST_URL + config.POST_SUBURL)
    else:
        if response_code != 0:
            raise HTTPException("FOODAPI", response_data, config.POST_URL + config.POST_SUBURL)
        return True
