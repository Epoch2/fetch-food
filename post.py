import urllib
import httplib
import mail
import config
import passwd

def post(action, data={}):
    data["passwd"] = passwd.POST_PASSWD
    data["action"] = action
    data_encoded = urllib.urlencode(data)
    connection = httplib.HTTPConnection(config.POST_URL)

    try:
        connection.request("POST", config.POST_PAGE, data_encoded, config.POST_HEADERS)
    except httplib.HTTPException as e:
        if config.CONFIG_MAIL_ENABLED:
            mail.sendmail("FetchFood ERROR!", "Error requesting POST to " + config.POST_URL + config.POST_PAGE + " -> HTTPError")
        connection.close()
        sys.exit(1)
    response = connection.getresponse()
    response_data = response.read()

    if not (int(response_data[0]) == 0 and int(response_data[1]) == 0) and config.CONFIG_MAIL_ENABLED:
        mail.sendmail("FetchFood ERROR!", "Error requesting POST to " + config.POST_URL + config.POST_PAGE + " -> " + str(response_data))

    return True

def post_entries(entrylist):
    entrycount = 0
    for entry in entrylist:
        postdata = entry.get_data();
        try:
            post(config.ACTION_POST_FOOD, postdata)
        except FoodEntryException as e:
            if config.CONFIG_MAIL_ENABLED:
                mail.sendmail("FetchFood ERROR!", "Error generating entries -> " + str(e.exception))
            sys.exit(1)
        else:
            entrycount += 1
    return entrycount
