# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def __init__(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(318, 173)
        LoginForm.setStyleSheet("background-color: #EFEFEF;")
        self.header = QtWidgets.QLabel(LoginForm)
        self.header.setGeometry(QtCore.QRect(0, 0, 321, 51))
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
        self.Password = QtWidgets.QLineEdit(LoginForm)
        self.Password.setGeometry(QtCore.QRect(47, 70, 231, 31))
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
        self.Login = QtWidgets.QToolButton(LoginForm)
        self.Login.setGeometry(QtCore.QRect(110, 120, 93, 37))
        self.Login.setStyleSheet("background-color: white;")
        self.Login.setObjectName("Login")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.header.setText(_translate("LoginForm", "Login"))
        self.Password.setPlaceholderText(_translate("LoginForm", "Password"))
        self.Login.setText(_translate("LoginForm", "Login"))
