# -*- coding: utf-8 -*-
TARGET_URL = "http://www.amica.se:80/nackagymnasium"

FOOD_DEFAULT_TYPE = u"Extrarätt"
FOOD_UNKNOWN_TYPE = "UNKNOWN_TYPE"

POST_DEFAULT_HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
POST_TIMEOUT = 10

PORTALN_POST_URLS = ["http://www.portaln.se:80/skola/foodapi.php", "http://latest.portaln.se:80/skola/foodapi.php"]

PORTALN_ACTION = {"post_food" : "post_food",
                  "post_info" : "post_info",
                  "clear_table" : "clear_table"}

PORTALN_SCHOOL_ID = "ng"

ERROR_FATAL = {"clear_table" : False,
               "post_entry" : False,
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

AMICA_HEADERS = {"Accept" : "*/*",
                 "Accept-Charset" : "UTF-8,*",
                 "Accept-Language" : "en-US,en",
                 "Cache-Control" : "no-cache",
                 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
                 "DNT" : "1",
                 "Host" : "www.amica.se",
                 "Origin" : "http://www.amica.se",
                 "Referer" : "http://www.amica.se/Ata-hos-Amica/Restauranger/Stockholm/Nacka/Nacka-gymnasium/",
                 "User-Agent" : "Portaln - Skola (fetch-food)",
                 "X-MicrosoftAjax" : "Delta=true",
                 "X-Requested-With" : "XMLHttpRequest"}

EMAIL_INFO = {"server" : "send.one.com:2525",
              "user" : "server@jvester.se",
              "from" : "server@jvester.se",
              "to" : ["jv@jvester.se", "adam@adsa.se"]}

CONFIG = {"mail_enabled" : False,
          "mail_newline" : "\n"}

DEBUG = True