from smtplib import *
import ssl


class MailMan:
    def __init__(self):
        self.cdc = ssl.create_default_context()
        self.sender_email = "fakepsyche@gmail.com"
        self.app_password = "wldd cakd wvke pmsf"

    def send_email(self, sending_message, to_email):
        with SMTP_SSL("smtp.gmail.com", port=465, context=self.cdc) as server:
            server.login(self.sender_email, self.app_password)
            server.sendmail(self.sender_email, to_email, msg=sending_message)
