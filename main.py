import webbrowser
from pathlib import Path

from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow
from emailSend import EmailSender


SETTINGS_FILE = Path("settings.json")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        self.ui.errorLabelSettings.hide()
        self.ui.errorLabelEmail.hide()
        self.ui.errorLabelBulkEmail.hide()

        self.ui.saveBtn.clicked.connect(self._saveSettings)
        self.ui.sendEmailBtn.clicked.connect(self._sendEmail)
        self.ui.sendBulkBtn.clicked.connect(self._sendBulk)
        self.ui.openWebBtn.clicked.connect(self._openWebPage)

        if not self.__checkSettingsConfigIsExists():
            self.__createSettingsConfig()
        self.__settings = self.__loadSettings()
        self.__emailSender = EmailSender(self.__settings)

    @staticmethod
    def _openWebPage():
        webbrowser.open("https://help.mail.ru/mail/mailer/popsmtp")

    def __showErrorLabelSettings(self, message):
        self.ui.errorLabelSettings.setText(message)
        self.ui.errorLabelSettings.show()

    def __showErrorLabelEmail(self, message):
        self.ui.errorLabelEmail.setText(message)
        self.ui.errorLabelEmail.show()

    def __showErrorLabelBulkEmail(self, message):
        self.ui.errorLabelBulkEmail.setText(message)
        self.ui.errorLabelBulkEmail.show()

    @staticmethod
    def __checkSettingsConfigIsExists():
        return True if SETTINGS_FILE.exists() else False

    @staticmethod
    def __createSettingsConfig():
        __settings = {
            "host": "None",
            "port": "None",
            "email": "None",
            "password": "None"
        }
        with SETTINGS_FILE.open("w", encoding="utf-8") as __settingsConfig:
            json.dump(__settings, __settingsConfig, ensure_ascii=False, indent=4)

    def __loadSettings(self):
        with SETTINGS_FILE.open(encoding="utf-8") as __settingsConfig:
            __settings = json.load(__settingsConfig)
            self.ui.inputHostSettings.setText(__settings["host"])
            self.ui.inputPortSettings.setText(str(__settings["port"]))
            self.ui.inputEmailSettings.setText(__settings["email"])
            self.ui.inputPasswordSettings.setText(__settings["password"])
            return __settings

    def __saveSettings(self, __settings):
        self.__settings = __settings
        with SETTINGS_FILE.open("w", encoding="utf-8") as __settingsConfig:
            json.dump(__settings, __settingsConfig, ensure_ascii=False, indent=4)

    def _saveSettings(self):
        if self.__validateSettingsInput():
            host = self.ui.inputHostSettings.text()
            port = self.ui.inputPortSettings.text()
            email = self.ui.inputEmailSettings.text()
            password = self.ui.inputPasswordSettings.text()
            self.__saveSettings(
                dict(
                    host=host,
                    port=int(port),
                    email=email,
                    password=password
                )
            )

    def __validateSettingsInput(self):
        host = self.ui.inputHostSettings.text()
        port = self.ui.inputPortSettings.text()
        email = self.ui.inputEmailSettings.text()
        password = self.ui.inputPasswordSettings.text()
        if all([len(host), len(port), len(email), len(password)]):
            if not port.isdigit():
                self.__showErrorLabelSettings("Порт должен быть числового типа!")
                return False
            if not self.__emailSender.validateEmail(email):
                self.__showErrorLabelSettings("Невалидный Email!")
                return False
            self.ui.errorLabelSettings.hide()
            return True
        self.__showErrorLabelSettings("Все поля должны быть заполнены!")
        return False

    def _sendEmail(self):
        if self.__validateEmailInput():
            email = self.ui.inputEmail.text()
            subject = self.ui.inputSubjectEmail.text()
            message = self.ui.inputMessageEmail.toPlainText()
            self.__emailSender.sendEmail(email, subject, message)
            self.__clearSendEmailForm()

    def __clearSendEmailForm(self):
        self.ui.inputEmail.clear()
        self.ui.inputSubjectEmail.clear()
        self.ui.inputMessageEmail.clear()

    def __validateEmailInput(self):
        email = self.ui.inputEmail.text()
        subject = self.ui.inputSubjectEmail.text()
        message = self.ui.inputMessageEmail.toPlainText()
        if all([len(email), len(subject), len(message)]):
            if not self.__emailSender.validateEmail(email):
                self.__showErrorLabelEmail("Невалидный Email!")
                return False
            self.ui.errorLabelEmail.hide()
            return True
        self.__showErrorLabelEmail("Все поля должны быть заполнены!")
        return False

    def _sendBulk(self):
        if self.__validateBulkEmail():
            path = self.ui.fileWithEmailAddressesBulk.text()
            subject = self.ui.inputSubjectBulk.text()
            message = self.ui.inputMessageBulk.toPlainText()
            with Path(path).open(encoding="utf-8") as file:
                emails = file.read().split("\n")
            self.__emailSender.sendBulkEmail(emails, subject, message)
            self.__clearSendBulkEmail()

    def __clearSendBulkEmail(self):
        self.ui.fileWithEmailAddressesBulk.clear()
        self.ui.inputSubjectBulk.clear()
        self.ui.inputMessageBulk.clear()

    def __validateBulkEmail(self):
        path = self.ui.fileWithEmailAddressesBulk.text()
        subject = self.ui.inputSubjectBulk.text()
        message = self.ui.inputMessageBulk.toPlainText()
        if all([len(path), len(subject), len(message)]):
            path = Path(path)
            if not path.exists() or not path.is_file():
                self.__showErrorLabelEmail("Не существующий файл!")
                return False
            self.ui.errorLabelEmail.hide()
            return True
        self.__showErrorLabelEmail("Все поля должны быть заполнены!")
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
