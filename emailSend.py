import smtplib
from email_validator import validate_email, EmailNotValidError
from logger import logger


log = logger.getLogger("emailSender")


class EmailSender:
    def __init__(self, __settings):
        self.__settings = __settings

    def sendEmail(self, email, subject, message):
        sender = self.__settings["email"]
        sender_password = self.__settings["password"]
        mail_lib = smtplib.SMTP_SSL(self.__settings["host"], self.__settings["port"])
        mail_lib.login(sender, sender_password)
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
        sender, email, subject)
        msg += message
        mail_lib.sendmail(sender, email, msg.encode('utf8'))
        log.info(f"Электронное письмо отправлено по адресу <{email}>")
        mail_lib.quit()

    def sendBulkEmail(self, emails, subject, message):
        sender = self.__settings["email"]
        sender_password = self.__settings["password"]
        mail_lib = smtplib.SMTP_SSL(self.__settings["host"], self.__settings["port"])
        mail_lib.login(sender, sender_password)
        for email in emails:
            if self.validateEmail(email):
                msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
                    sender, email, subject)
                msg += message
                mail_lib.sendmail(sender, email, msg.encode('utf8'))
                log.info(f"Электронное письмо отправлено по адресу <{email}>")
            else:
                log.error(f"Не валидный Email <{email}>")
        mail_lib.quit()

    @staticmethod
    def validateEmail(email):
        try:
            validatedEmail = validate_email(email)
            email = validatedEmail["email"]
            return True
        except EmailNotValidError:
            return False
