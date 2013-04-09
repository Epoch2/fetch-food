import urllib2
import urllib
import httplib
import mail
import config
import passwd

class HTTPException(Exception):

    def __init__(self, type_, exception, url):
        self.type_ = type_
        self.exception = exception
        self.url = url

    def __str__(self):
        return self.type_ + ": " + str(self.exception) + " -> " + self.url

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

def post_data(url, headers, data):
    data_encoded = urllib.urlencode(data)
    request = urllib2.Request(url, data_encoded, headers)
    try:
        page = urllib2.urlopen(request, timeout=config.POST_TIMEOUT)
    except urllib2.HTTPError as e:
        raise HTTPException("POST", e, url)
    except urllib2.URLError as e:
        raise HTTPException("POST", e, url)
    else:
        page_content = page.read()
        page.close()
        return page_content

def post_portaln(url, action, data={}):
    data["action"] = action
    data["school"] = config.PORTALN_SCHOOL_ID
    data["passwd"] = passwd.PORTALN_POST_PASSWD

    try:
        response = post_data(url, config.POST_DEFAULT_HEADERS, data)
    except HTTPException as e:
        raise
    else:
        response = response.replace("\n", "").strip()

    try:
        response_code = int(response[0] + response[1])
    except ValueError:
        raise HTTPException("PORTALN.SE", "Internal server error", config.POST_URL)
    else:
        if response_code != 0:
            raise HTTPException("FOODAPI", response, config.POST_URL)
        else:
            return True
