import sys
import mail
import datehelper
import post
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

    def compile_error(self, error):
        if type(error) == post.PostException:
            return error.type_ + " :" + error.exception + " -> " + error.url
        else:
            return str(error)

    def get_errors_compiled(self, delimiter="\n"):
        errorlist_compiled = []
        for error in self.errorlist:
            errorlist_compiled.append(self.compile_error(error))
        return "".join(errorlist_compiled)

    def send_fatal(self, error):
        if config.CONFIG_MAIL_ENABLED:
            mail_subject = "FetchFood FAILED!"
            mail_content = ("A fatal error occurred at:\n\n" +
                            datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_DATE) + "\n" +
                            datehelper.to_string(datehelper.current_date(), datehelper.PRECISION_TIME) + "\n\n" +
                            "FATAL ERROR: " + self.compile_error(error) + "\n\n" +
                            "These additional (non-fatal) errors occurred during program execution:" + "\n" +
                            self.get_errors_compiled("\n"))
            mail.sendmail(mail_subject, mail_content)
        sys.exit(1)
