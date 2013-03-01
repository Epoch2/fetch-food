# -*- coding: utf-8 -*-
TARGET_URL = "http://www.amica.se:80/nackagymnasium"

FOOD_DEFAULT_TYPE = u"Extrarätt"
FOOD_UNKNOWN_TYPE = "UNKNOWN_TYPE"

POST_DEFAULT_HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

PORTALN_POST_URL = "www.portaln.se:80/skola/foodapi.php"

PORTALN_ACTION = {"post_food" : "post_food",
                  "post_info" : "post_info",
                  "clear_table" : "clear_table"}

ERROR_FATAL = {"clear_table" : True,
               "post_entry" : True,
               "post_info" : False,
               "postback" : True}

AMICA_TYPE_KEY = "ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenu"
AMICA_WEEK_KEY = "ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek"

AMICA_POST_DATA = {"ctl00$RegionPageBody$DefaultScriptManager" : "ctl00$RegionPageBody$DefaultScriptManager|ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek",
                   "ctl00$RegionPageBody$RegionHeader$ctl00$ctl01$SearchText" : "",
                   "__ASYNCPOST" : "true",
                   "__EVENTTARGET" : "ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek",
                   "__EVENTARGUMENT" : "",
                   "__LASTFOCUS" : "",
                   "" : ""}

EMAIL_INFO = {"server" : "send.one.com:2525",
              "user" : "server@jvester.se",
              "from" : "server@jvester.se",
              "to" : "jv@jvester.se"}

CONFIG = {"mail_enabled" : True,
          "mail_newline" : "\n"}
