import os
import config
import passwd

def sendmail(subject, content):
    for recipient in config.EMAIL_INFO["to"]:
        os.system("sendemail -q -f " + config.EMAIL_INFO["from"] + " -t " + recipient + " -s " + config.EMAIL_INFO["server"] + " -xu " + config.EMAIL_INFO["user"] + " -xp " + passwd.EMAIL_PASSWD + " -u " + subject + " -m " + content)
