import smtplib


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
        mail_lib.quit()

    def sendBulkEmail(self, emails, message):
        sender = self.__settings["email"]
        sender_password = self.__settings["password"]
        mail_lib = smtplib.SMTP_SSL(self.__settings["host"], self.__settings["port"])
        mail_lib.login(sender, sender_password)
        for email in emails:
            msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
                sender, email, 'Тема сообщения')
            msg += message
            mail_lib.sendmail(sender, email, msg.encode('utf8'))
        mail_lib.quit()
