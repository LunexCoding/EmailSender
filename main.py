import json
from pathlib import Path

from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow


SETTINGS_FILE = Path("settings.json")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        self.ui.saveBtn.clicked.connect(self._saveSettings)
        self.ui.sendEmailBtn.clicked.connect(self._sendEmail)
        self.ui.sendBulkBtn.clicked.connect(self._sendBulk)

        self.__settings = self.__loadSettings()

    def __loadSettings(self):
        with SETTINGS_FILE.open(encoding="utf-8") as settings:
            return json.load(settings)

    def _saveSettings(self):
        ...

    def _sendEmail(self):
        ...

    def _sendBulk(self):
        ...




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
