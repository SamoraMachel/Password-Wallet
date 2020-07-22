# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupForm(object):
    def __init__(self, SetupForm):
        SetupForm.setObjectName("SetupForm")
        SetupForm.resize(309, 253)
        SetupForm.setStyleSheet("background-color: #EFEFEF;")
        self.header = QtWidgets.QLabel(SetupForm)
        self.header.setGeometry(QtCore.QRect(-10, 0, 321, 51))
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
        self.Username = QtWidgets.QLineEdit(SetupForm)
        self.Username.setGeometry(QtCore.QRect(40, 80, 231, 31))
        self.Username.setStyleSheet("#Username{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"\n"
"#Username:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLineEdit(SetupForm)
        self.Password.setGeometry(QtCore.QRect(40, 130, 231, 31))
        self.Password.setStyleSheet("#Password{\n"
"    background-color: rgba(255, 255, 255, 0.8);\n"
"    border-radius: 15px;    \n"
"    border: 1px solid #D9D9D9;\n"
"}\n"
"\n"
"#Password:focus{\n"
"    background-color: white;\n"
"    border-radius: 0px;    \n"
"    border-color: rgba(64, 144, 218, 1);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    text-indent: 10px;\n"
"}")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Password.setObjectName("Password")
        self.Setup = QtWidgets.QToolButton(SetupForm)
        self.Setup.setGeometry(QtCore.QRect(100, 190, 93, 37))
        self.Setup.setStyleSheet("background-color: white;")
        self.Setup.setObjectName("Setup")

        self.retranslateUi(SetupForm)
        QtCore.QMetaObject.connectSlotsByName(SetupForm)

    def retranslateUi(self, SetupForm):
        _translate = QtCore.QCoreApplication.translate
        SetupForm.setWindowTitle(_translate("SetupForm", "Setup"))
        self.header.setText(_translate("SetupForm", "Setup"))
        self.Username.setPlaceholderText(_translate("SetupForm", "Username"))
        self.Password.setPlaceholderText(_translate("SetupForm", "Password"))
        self.Setup.setText(_translate("SetupForm", "Setup"))
