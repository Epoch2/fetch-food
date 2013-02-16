import os
import config
import passwd

def sendmail(subject, content):
     os.system(("sendemail -q -f " + config.EMAIL_FROM + " -t " + config.EMAIL_TO + " -s " + config.EMAIL_SERVER + " -xu " + config.EMAIL_USER + " -xp " + passwd.EMAIL_PASSWD + " -u " + subject + " -m " + content))
