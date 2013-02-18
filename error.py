import mail
import datehelper
import config
import sys

class ErrorHandler:

    def __init__(self):
        self.errorlist = []
        self.has_error = False

    def add_error(self, error, fatal):
        print fatal
        if fatal:
            self.send_fatal(error)
        self.errorlist.append(error)
        self.has_error = True

    def compile_error(self, error):
        if type(error) == PostException:
            return error.type_, + " :" + error.exception + " -> " + error.url

    def get_errors_compiled(self, delimiter="\n"):
        errorlist_compiled = []
        for error in self.errorlist:
            if type(error) == PostException:
                errorlist_compiled.append(error.type_, + " :" + error.exception + " -> " + error.url + delimiter)
        return "".join(errorlist_compiled)

    def send_fatal(self, error):
        print "sendfatal"
        mail_subject = "FetchFood FAILED!"
        mail_content = ("A fatal error occurred at:\n\n" +
                        datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + "\n" +
                        datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + "\n\n" +
                        "FATAL ERROR: " + str(error) + "\n\n" +
                        "These additional (non-fatal) errors occurred during program execution:" + "\n" +
                        self.get_errors_compiled("\n"))
        if config.CONFIG_MAIL_ENABLED:
            mail.sendmail(mail_subject, mail_content)
        else:
            print mail_content
        sys.exit(1)
        return
