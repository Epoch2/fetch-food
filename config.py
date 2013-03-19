# -*- coding: utf-8 -*-
TARGET_URL = "http://www.amica.se:80/nackagymnasium"

FOOD_DEFAULT_TYPE = u"Extrarätt"
FOOD_UNKNOWN_TYPE = "UNKNOWN_TYPE"

POST_DEFAULT_HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

PORTALN_POST_URL = "http://www.portaln.se:80/skola/foodapi.php"

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

AMICA_HEADERS = {"Accept" : "*/*",
                 "Accept-Charset" : "UTF-8,*",
                 "Accept-Language" : "en-US,en",
                 "Cache-Control" : "no-cache",
                 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
                 "DNT" : "1",
                 "Host" : "www.amica.se",
                 "Origin" : "http://www.amica.se",
                 "Referer" : "http://www.amica.se/Ata-hos-Amica/Restauranger/Stockholm/Nacka/Nacka-gymnasium/",
                 "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.155 Safari/537.22",
                 "X-MicrosoftAjax" : "Delta=true",
                 "X-Requested-With" : "XMLHttpRequest"}

EMAIL_INFO = {"server" : "send.one.com:2525",
              "user" : "server@jvester.se",
              "from" : "server@jvester.se",
              "to" : "jv@jvester.se"}

CONFIG = {"mail_enabled" : True,
          "mail_newline" : "\n"}
