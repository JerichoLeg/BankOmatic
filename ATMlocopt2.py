# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ATMlocop2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(540, 360)
        SecondWindow.setMinimumSize(QtCore.QSize(540, 360))
        SecondWindow.setMaximumSize(QtCore.QSize(540, 360))
        SecondWindow.setMouseTracking(True)
        SecondWindow.setStyleSheet("*{\n"
"font-family: Akrobat;\n"
"}\n"
"QMainWindow{\n"
"border-image:url(:/images/BG.jpg)\n"
"}\n"
"QLabel{\n"
"font-family: Akrobat;\n"
"font-size: 22px;\n"
"}\n"
"QToolButton{\n"
"background: transparent\n"
"}\n"
"QToolButton:hover{\n"
"background: #E0ECF8;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton{\n"
"color:#dfdfdf;\n"
"background:#00264d;\n"
"border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"background: #dfdfdf;\n"
"font-size:15px;\n"
"}\n"
"QLineEdit:hover{\n"
"border-radius:10px;\n"
"background: #ffffff;\n"
"}\n"
"Qlabel{\n"
"color:#dfdfdf;\n"
"background:transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(500, 10, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(180, 0, 181, 121))
        self.label_logo.setStyleSheet("image: url(:/images/Logo.png)")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.commandLinkButton.setMouseTracking(True)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 80, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 330, 121, 41))
        self.label_2.setObjectName("label_2")
        self.enterLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.enterLocation.setGeometry(QtCore.QRect(180, 300, 201, 21))
        self.enterLocation.setMinimumSize(QtCore.QSize(181, 0))
        font = QtGui.QFont()
        font.setFamily("Akrobat")
        font.setPointSize(-1)
        self.enterLocation.setFont(font)
        self.enterLocation.setText("")
        self.enterLocation.setReadOnly(False)
        self.enterLocation.setClearButtonEnabled(True)
        self.enterLocation.setObjectName("enterLocation")
        self.searchIcon = QtWidgets.QToolButton(self.centralwidget)
        self.searchIcon.setGeometry(QtCore.QRect(380, 300, 21, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/iconfinder_Search_858732.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchIcon.setIcon(icon1)
        self.searchIcon.setIconSize(QtCore.QSize(40, 40))
        self.searchIcon.setCheckable(True)
        self.searchIcon.setObjectName("searchIcon")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(110, 120, 341, 171))
        self.webEngineView.setUrl(QtCore.QUrl("file:///ATMMap2.html"))
        self.webEngineView.setObjectName("webEngineView")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        self.toolButton.clicked.connect(SecondWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "ATM Locator"))
        self.toolButton.setText(_translate("SecondWindow", "..."))
        self.commandLinkButton.setText(_translate("SecondWindow", "Back to Main Menu"))
        self.label.setText(_translate("SecondWindow", "ATM Locator"))
        self.label_2.setText(_translate("SecondWindow", "ATM Locator"))
        self.enterLocation.setPlaceholderText(_translate("SecondWindow", "               Enter your location"))
        self.searchIcon.setText(_translate("SecondWindow", "..."))
from PyQt5 import QtWebEngineWidgets
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())