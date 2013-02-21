import sys
import mail
import datehelper
import config

class ErrorHandler:

    def __init__(self):
        self.errorlist = []
        self.has_error = False

    def add_error(self, error, fatal):
        if fatal:
            self.send_fatal(error)
        self.errorlist.append(error)
        self.has_error = True

    def get_errors_compiled(self, delimiter="\n"):
        errorlist_compiled = []
        for error in self.errorlist:
            errorlist_compiled.append(str(error))
        return "".join(errorlist_compiled)

    def send_fatal(self, error):
        nl = config.CONFIG["mail_newline"]
        if config.CONFIG["mail_enabled"]:
            mail_subject = "FetchFood FAILED!"
            mail_content = ("A fatal error occurred at:" + nl + nl +
                            datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + nl +
                            datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + nl + nl +
                            "FATAL ERROR: " + str(error) + nl + nl +
                            "These additional (non-fatal) errors occurred during program execution:" + nl +
                            self.get_errors_compiled(nl))
            mail.sendmail(mail_subject, mail_content)
        sys.exit(1)
