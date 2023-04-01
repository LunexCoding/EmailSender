import json
from pathlib import Path

from Custom_Widgets.Widgets import *

from email_validator import validate_email, EmailNotValidError

from forms.ui_interface import Ui_MainWindow


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

        self.ui.saveBtn.clicked.connect(self._saveSettings)
        self.ui.sendEmailBtn.clicked.connect(self._sendEmail)
        self.ui.sendBulkBtn.clicked.connect(self._sendBulk)

        if not self.__checkSettingsConfigIsExists():
            self.__createSettingsConfig()
        self.__settings = self.__loadSettings()

    def __showErrorLabelSettings(self, message):
        self.ui.errorLabelSettings.setText(message)
        self.ui.errorLabelSettings.show()

    def __showErrorLabelEmail(self, message):
        self.ui.errorLabelSettings.setText(message)
        self.ui.errorLabelEmail.show()

    def __checkSettingsConfigIsExists(self):
        return True if SETTINGS_FILE.exists() else False

    def __createSettingsConfig(self):
        __settings = {
            "host": "None",
            "port": "None",
            "email": "None",
            "password": "None"
        }
        with SETTINGS_FILE.open("w", encoding="utf-8") as settingsConfig:
            json.dump(__settings, settingsConfig, ensure_ascii=False, indent=4)

    def __loadSettings(self):
        with SETTINGS_FILE.open(encoding="utf-8") as settings:
            return json.load(settings)

    def __saveSettings(self, __settings):
        self.__settings = __settings
        with SETTINGS_FILE.open("w", encoding="utf-8") as settingsConfig:
            json.dump(__settings, settingsConfig, ensure_ascii=False, indent=4)

    def _saveSettings(self):
        if self.__validateSettingsInput():
            host = self.ui.inputHostSettings.text()
            port = self.ui.inputPortSettings.text()
            email = self.ui.inputEmail.text()
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
        email = self.ui.inputEmail.text()
        password = self.ui.inputPasswordSettings.text()
        if all([len(host), len(port), len(email), len(password)]):
            if not port.isdigit():
                self.__showErrorLabelSettings("Порт должен быть числового типа!")
                return False
            if not self.__validateEmail(email):
                self.__showErrorLabelSettings("Невалидный Email!")
                return False
            self.ui.errorLabelSettings.hide()
            return True
        self.__showErrorLabelSettings("Все поля должны быть заполнены!")
        return False

    def __validateEmail(self, email):
        try:
            validatedEmail = validate_email(email)
            email = validatedEmail["email"]
            return True
        except EmailNotValidError as e:
            return False

    def _sendEmail(self):
        if self.__validateEmailInput():
            ...

    def __validateEmailInput(self):
        email = self.ui.inputEmail.text()
        subject = self.ui.inputSubjectEmail.text()
        message = self.ui.inputMessageEmail.text()
        if all([len(email), len(subject), len(message)]):
            if not self.__validateEmail(email):
                self.__showErrorLabelEmail("Невалидный Email!")
                return False
            self.ui.errorLabelEmail.hide()
            return True
        self.__showErrorLabelEmail("Все поля должны быть заполнены!")
        return False

    def _sendBulk(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
