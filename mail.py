import os
import config
import passwd

def sendmail(subject, content):
    return
    os.system("sendemail -q -f " + config.EMAIL_INFO["from"] + " -t " + config.EMAIL_INFO["to"] + " -s " + config.EMAIL_INFO["server"] + " -xu " + config.EMAIL_INFO["user"] + " -xp " + passwd.EMAIL_PASSWD + " -u " + subject + " -m " + content)
