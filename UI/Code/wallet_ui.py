# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wallet.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: #EFEFEF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 69, 89, 35))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 160, 89, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 114, 89, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(19)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.header.setFont(font)
        self.header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.header.setStyleSheet("#header{\n"
"    background-color: teal;\n"
"    color: white;\n"
"}")
        self.header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.header.setTextFormat(QtCore.Qt.RichText)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(20, 109, 231, 31))
        self.Email.setStyleSheet("#Email{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;    \n"
"}\n"
"\n"
"#Email:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Email.setObjectName("Email")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(20, 151, 231, 31))
        self.Password.setStyleSheet("#Password{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"#Password:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.URL = QtWidgets.QLineEdit(self.centralwidget)
        self.URL.setGeometry(QtCore.QRect(20, 193, 231, 31))
        self.URL.setStyleSheet("#URL{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"\n"
"#URL:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.URL.setObjectName("URL")
        self.Title = QtWidgets.QLineEdit(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(19, 65, 231, 31))
        self.Title.setStyleSheet("#Title{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"\n"
"#Title:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Title.setObjectName("Title")
        self.Message = QtWidgets.QTextEdit(self.centralwidget)
        self.Message.setGeometry(QtCore.QRect(20, 239, 381, 189))
        self.Message.setStyleSheet("#Message{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"\n"
"#Message:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Message.setObjectName("Message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.webView = QtWebKitWidgets.QWebView(self.dockWidgetContents_2)
        self.webView.setGeometry(QtCore.QRect(-1, -11, 431, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Wallet"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Database"))
        self.pushButton_3.setText(_translate("MainWindow", "View"))
        self.header.setText(_translate("MainWindow", "Password Wallet"))
        self.Email.setPlaceholderText(_translate("MainWindow", "Email or Phone"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.URL.setPlaceholderText(_translate("MainWindow", "URL"))
        self.Title.setPlaceholderText(_translate("MainWindow", "Title"))
        self.Message.setPlaceholderText(_translate("MainWindow", "Description or Message"))
        self.dockWidget.setToolTip(_translate("MainWindow", "WebBrowser"))
        self.actionOpen_File.setText(_translate("MainWindow", "Clear"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
from PyQt5 import QtWebKitWidgets