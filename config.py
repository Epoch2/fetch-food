# -*- coding: utf-8 -*-
TARGET_URL = "http://www.amica.se:80"
TARGET_SUBURL = "/nackagymnasium"
TARGET_CONTENT_IDENTIFIER = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_MenuUpdatePanel div[class-=ContentArea] p"
TARGET_CURRENT_DATE_IDENTIFIER = "h2#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_HeadingMenu"
TARGET_SELECTABLE_DATE_IDENTIFIER = "div#ctl00_RegionPageBody_RegionPage_RegionContent_RegionMainContent_RegionMainContentMiddle_MainContentMenu_ctl00_ctl01 select[name=ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek] option"

FOOD_DEFAULT_TYPE = u"Extrarätt"
FOOD_UNKNOWN_TYPE = "UNKNOWN_TYPE"

ACTION_POST_FOOD = "post_food"
ACTION_POST_INFO = "post_info"
ACTION_CLEAR_TABLE = "clear_table"

ERROR_CLEAR_TABLE_FATAL = True
ERROR_POST_ENTRY_FATAL = True
ERROR_POST_INFO_FATAL = False

POST_TYPE_TYPE = "type"
POST_TYPE_TIME = "time"

AMICA_TYPE_KEY = "ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenu"
AMICA_WEEK_KEY = "ctl00$RegionPageBody$RegionPage$RegionContent$RegionMainContent$RegionMainContentMiddle$MainContentMenu$ctl00$DropDownListMenuWeek"

POST_URL = "www.portaln.se:80"
POST_SUBURL = "/skola/foodapi.php"
POST_DEFAULT_HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

EMAIL_SERVER = "send.one.com:2525"
EMAIL_USER = "server@jvester.se"
EMAIL_FROM = "server@jvester.se"
EMAIL_TO = "jv@jvester.se"

CONFIG_MAIL_ENABLED = False
CONFIG_MAIL_NEWLINE = "\r"
