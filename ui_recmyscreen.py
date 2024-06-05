# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designRjCYTN.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 562)
        MainWindow.setWindowTitle(u"RecMyScreen")
        icon = QIcon()
        icon.addFile(u":/icons/video_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 111, 157)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bg = QLabel(self.centralwidget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(-10, -20, 791, 681))
        self.bg.setPixmap(QPixmap(u":/backgrounds/background.png"))
        self.appTitle = QLabel(self.centralwidget)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(150, 30, 278, 72))
        self.appTitle.setStyleSheet(u"background-color: teal;\n"
"color: yellow;\n"
"padding: 15px;\n"
"text-align: center;\n"
"\n"
"font-size: 37px;\n"
"font-family: Arial, verdana, sans-serif;")
        self.app_desc = QLabel(self.centralwidget)
        self.app_desc.setObjectName(u"app_desc")
        self.app_desc.setGeometry(QRect(200, 160, 175, 33))
        self.app_desc.setStyleSheet(u"font-size: 29px;\n"
"font-family: \"Agency FB\", sans-serif;\n"
"color: khaki;\n"
"background-color: olive;")
        self.playbtn = QPushButton(self.centralwidget)
        self.playbtn.setObjectName(u"playbtn")
        self.playbtn.setEnabled(True)
        self.playbtn.setGeometry(QRect(90, 310, 75, 71))
        self.playbtn.setStyleSheet(u"\n"
"width: 33px;\n"
"border-radius: 25%;\n"
"border: 3px solid white;\n"
"outline: 3px solid red;\n"
"background-color: yellow;\n"
"font-size: 22px;\n"
"\n"
"icon-size: 128px;")
        icon1 = QIcon()
        icon1.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playbtn.setIcon(icon1)
        self.pausebtn = QPushButton(self.centralwidget)
        self.pausebtn.setObjectName(u"pausebtn")
        self.pausebtn.setEnabled(False)
        self.pausebtn.setGeometry(QRect(240, 310, 75, 71))
        self.pausebtn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"width: 33px;\n"
"border-radius: 25%;\n"
"background-color: yellow;\n"
"font-size: 22px;\n"
"\n"
"icon-size: 128px;")
        icon2 = QIcon()
        icon2.addFile(u":/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pausebtn.setIcon(icon2)
        self.stopbtn = QPushButton(self.centralwidget)
        self.stopbtn.setObjectName(u"stopbtn")
        self.stopbtn.setEnabled(False)
        self.stopbtn.setGeometry(QRect(390, 310, 75, 71))
        self.stopbtn.setStyleSheet(u"border: none;\n"
"outline: none;\n"
"width: 33px;\n"
"border-radius: 25%;\n"
"background-color: yellow;\n"
"font-size: 22px;\n"
"\n"
"icon-size: 128px;")
        icon3 = QIcon()
        icon3.addFile(u":/images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopbtn.setIcon(icon3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.bg.setText("")
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"RecMyScreen", None))
        self.app_desc.setText(QCoreApplication.translate("MainWindow", u"Record your screen.", None))
        self.playbtn.setText("")
        self.pausebtn.setText("")
        self.stopbtn.setText("")

        pass
    # retranslateUi

