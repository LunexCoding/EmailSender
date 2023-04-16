# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXmjiPX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 500)
        MainWindow.setMinimumSize(QSize(0, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"* {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#leftMenuSubContainer QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer {\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: "
                        "10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"#saveIngredientBtn {\n"
"	margin-top: 30px;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
""
                        "QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR */\n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
""
                        "QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"	background-color: #262a30;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	width: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-top-left-radius: 7px;\n"
"	subcontrol-position: right;"
                        "\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"	background-color:#262a30;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {	\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setAutoFillBackground(False)
        self.leftMenuSubContainer.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setPointSize(10)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.singleMailBtn = QPushButton(self.frame_2)
        self.singleMailBtn.setObjectName(u"singleMailBtn")
        self.singleMailBtn.setFont(font)
        self.singleMailBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.singleMailBtn.setIcon(icon2)
        self.singleMailBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.singleMailBtn)

        self.bulkEmailBtn = QPushButton(self.frame_2)
        self.bulkEmailBtn.setObjectName(u"bulkEmailBtn")
        self.bulkEmailBtn.setFont(font)
        self.bulkEmailBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bulkEmailBtn.setIcon(icon3)
        self.bulkEmailBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.bulkEmailBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setAutoFillBackground(False)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        font1 = QFont()
        font1.setPointSize(12)
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 25))
        self.label_5.setPixmap(QPixmap(u":/icons/mail.svg"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(527, 351))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setMinimumSize(QSize(0, 0))
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_25 = QVBoxLayout(self.pageHome)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_31 = QFrame(self.pageHome)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 100))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, 0, -1)
        self.label_16 = QLabel(self.frame_32)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_16)


        self.horizontalLayout_18.addWidget(self.frame_32, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_31)

        self.frame_33 = QFrame(self.pageHome)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_33)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_34)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_35)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.frame_36)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setWordWrap(False)

        self.horizontalLayout_20.addWidget(self.label_11)

        self.openWebBtn = QPushButton(self.frame_36)
        self.openWebBtn.setObjectName(u"openWebBtn")
        self.openWebBtn.setFont(font1)
        self.openWebBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openWebBtn.setIcon(icon8)
        self.openWebBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.openWebBtn)


        self.verticalLayout_28.addWidget(self.frame_36, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.frame_37)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_21.addWidget(self.label_17)

        self.openSettingsBtn = QPushButton(self.frame_37)
        self.openSettingsBtn.setObjectName(u"openSettingsBtn")
        self.openSettingsBtn.setFont(font1)
        self.openSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.openSettingsBtn.setIcon(icon4)
        self.openSettingsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_21.addWidget(self.openSettingsBtn)


        self.verticalLayout_28.addWidget(self.frame_37, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_27.addWidget(self.frame_35, 0, Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.frame_34)


        self.verticalLayout_25.addWidget(self.frame_33)

        self.mainPages.addWidget(self.pageHome)
        self.emailPage = QWidget()
        self.emailPage.setObjectName(u"emailPage")
        self.verticalLayout_24 = QVBoxLayout(self.emailPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_23 = QFrame(self.emailPage)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 100))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_23)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(16777215, 16777215))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_14)


        self.verticalLayout_29.addWidget(self.frame_24, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.errorLabelEmail = QLabel(self.frame_23)
        self.errorLabelEmail.setObjectName(u"errorLabelEmail")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.errorLabelEmail.setFont(font4)
        self.errorLabelEmail.setStyleSheet(u"color: red;")

        self.verticalLayout_29.addWidget(self.errorLabelEmail, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.emailPage)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_25)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_26)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_27)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_27)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.label_9)


        self.verticalLayout_20.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.inputEmail = QLineEdit(self.frame_28)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setMinimumSize(QSize(350, 0))
        self.inputEmail.setMaximumSize(QSize(350, 16777215))
        self.inputEmail.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.inputEmail)


        self.verticalLayout_20.addWidget(self.frame_28, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_20.addWidget(self.label_10)

        self.inputSubjectEmail = QLineEdit(self.frame_26)
        self.inputSubjectEmail.setObjectName(u"inputSubjectEmail")
        self.inputSubjectEmail.setClearButtonEnabled(True)

        self.verticalLayout_20.addWidget(self.inputSubjectEmail)


        self.verticalLayout_19.addWidget(self.frame_26)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_29)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.inputMessageEmail = QTextEdit(self.frame_29)
        self.inputMessageEmail.setObjectName(u"inputMessageEmail")
        self.inputMessageEmail.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_22.addWidget(self.inputMessageEmail)


        self.verticalLayout_19.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sendEmailBtn = QPushButton(self.frame_30)
        self.sendEmailBtn.setObjectName(u"sendEmailBtn")
        self.sendEmailBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendEmailBtn.setIcon(icon9)
        self.sendEmailBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.sendEmailBtn)


        self.verticalLayout_19.addWidget(self.frame_30, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.frame_25)

        self.mainPages.addWidget(self.emailPage)
        self.bulkEmailPage = QWidget()
        self.bulkEmailPage.setObjectName(u"bulkEmailPage")
        self.verticalLayout_9 = QVBoxLayout(self.bulkEmailPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_13 = QFrame(self.bulkEmailPage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 100))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 0))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_12)


        self.verticalLayout_30.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.errorLabelBulkEmail = QLabel(self.frame_13)
        self.errorLabelBulkEmail.setObjectName(u"errorLabelBulkEmail")
        self.errorLabelBulkEmail.setFont(font4)
        self.errorLabelBulkEmail.setStyleSheet(u"color: red;")

        self.verticalLayout_30.addWidget(self.errorLabelBulkEmail, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_4 = QFrame(self.bulkEmailPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fileWithEmailAddressesBulk = QLineEdit(self.frame_9)
        self.fileWithEmailAddressesBulk.setObjectName(u"fileWithEmailAddressesBulk")
        self.fileWithEmailAddressesBulk.setMinimumSize(QSize(350, 0))
        self.fileWithEmailAddressesBulk.setMaximumSize(QSize(350, 16777215))
        self.fileWithEmailAddressesBulk.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.fileWithEmailAddressesBulk)


        self.verticalLayout_6.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.inputSubjectBulk = QLineEdit(self.frame_6)
        self.inputSubjectBulk.setObjectName(u"inputSubjectBulk")
        self.inputSubjectBulk.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.inputSubjectBulk)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.inputMessageBulk = QTextEdit(self.frame_11)
        self.inputMessageBulk.setObjectName(u"inputMessageBulk")
        self.inputMessageBulk.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_8.addWidget(self.inputMessageBulk)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sendBulkBtn = QPushButton(self.frame_12)
        self.sendBulkBtn.setObjectName(u"sendBulkBtn")
        self.sendBulkBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendBulkBtn.setIcon(icon9)
        self.sendBulkBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.sendBulkBtn)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.mainPages.addWidget(self.bulkEmailPage)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.verticalLayout_23 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 0, 10, 0)
        self.frame_15 = QFrame(self.pageSettings)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 100))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_13)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.errorLabelSettings = QLabel(self.frame_15)
        self.errorLabelSettings.setObjectName(u"errorLabelSettings")
        self.errorLabelSettings.setFont(font4)
        self.errorLabelSettings.setStyleSheet(u"color: #FF0000;")

        self.verticalLayout_11.addWidget(self.errorLabelSettings, 0, Qt.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_15)

        self.frame_18 = QFrame(self.pageSettings)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_16 = QFrame(self.frame_18)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 265))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 9)
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_13.addWidget(self.label_3)

        self.inputHostSettings = QLineEdit(self.frame_19)
        self.inputHostSettings.setObjectName(u"inputHostSettings")
        self.inputHostSettings.setMinimumSize(QSize(150, 0))
        self.inputHostSettings.setMaximumSize(QSize(250, 16777215))
        self.inputHostSettings.setClearButtonEnabled(True)

        self.verticalLayout_13.addWidget(self.inputHostSettings)


        self.verticalLayout_12.addWidget(self.frame_19, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_20)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_14.addWidget(self.label_4)

        self.inputPortSettings = QLineEdit(self.frame_20)
        self.inputPortSettings.setObjectName(u"inputPortSettings")
        self.inputPortSettings.setMinimumSize(QSize(100, 0))
        self.inputPortSettings.setMaximumSize(QSize(60, 16777215))
        self.inputPortSettings.setClearButtonEnabled(True)

        self.verticalLayout_14.addWidget(self.inputPortSettings)


        self.verticalLayout_12.addWidget(self.frame_20, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_21 = QFrame(self.frame_16)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_16.addWidget(self.label_7)

        self.inputEmailSettings = QLineEdit(self.frame_21)
        self.inputEmailSettings.setObjectName(u"inputEmailSettings")
        self.inputEmailSettings.setMinimumSize(QSize(200, 0))
        self.inputEmailSettings.setMaximumSize(QSize(150, 16777215))
        self.inputEmailSettings.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.inputEmailSettings)


        self.verticalLayout_12.addWidget(self.frame_21, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 20)
        self.label_8 = QLabel(self.frame_22)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_17.addWidget(self.label_8)

        self.inputPasswordSettings = QLineEdit(self.frame_22)
        self.inputPasswordSettings.setObjectName(u"inputPasswordSettings")
        self.inputPasswordSettings.setMinimumSize(QSize(150, 0))
        self.inputPasswordSettings.setMaximumSize(QSize(150, 16777215))
        self.inputPasswordSettings.setClearButtonEnabled(True)

        self.verticalLayout_17.addWidget(self.inputPasswordSettings)


        self.verticalLayout_12.addWidget(self.frame_22, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.saveBtn = QPushButton(self.frame_16)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBtn.setIcon(icon10)
        self.saveBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.saveBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_18)

        self.mainPages.addWidget(self.pageSettings)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.singleMailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"My Recipes", None))
#endif // QT_CONFIG(tooltip)
        self.singleMailBtn.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
#if QT_CONFIG(tooltip)
        self.bulkEmailBtn.setToolTip(QCoreApplication.translate("MainWindow", u"My Ingredients", None))
#endif // QT_CONFIG(tooltip)
        self.bulkEmailBtn.setText(QCoreApplication.translate("MainWindow", u"Mailing of emails", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.headerContainer.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"EmailSender", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"EmailSender", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0437\u043d\u0430\u043a\u043e\u043c\u044c\u0442\u0435\u0441\u044c \u0441 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0435\u0439 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0435 SMTP:", None))
        self.openWebBtn.setText(QCoreApplication.translate("MainWindow", u" \u041e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u0442\u0435 SMTP:", None))
        self.openSettingsBtn.setText(QCoreApplication.translate("MainWindow", u" \u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0433\u043e \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.errorLabelEmail.setText(QCoreApplication.translate("MainWindow", u"ErrorLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f:", None))
        self.inputMessageEmail.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.sendEmailBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u0440\u0430\u0441\u0441\u044b\u043b\u043a\u0438", None))
        self.errorLabelBulkEmail.setText(QCoreApplication.translate("MainWindow", u"errorLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0441 \u0430\u0434\u0440\u0435\u0441\u0430\u043c\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f:", None))
        self.inputMessageBulk.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.sendBulkBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.errorLabelSettings.setText(QCoreApplication.translate("MainWindow", u"ErrorLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SMTP Host:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SMTP Port:", None))
        self.inputPortSettings.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.saveBtn.setText("")
    # retranslateUi

