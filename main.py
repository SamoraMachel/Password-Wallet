# %% imports the UI code 
from UI.Code.login_ui import Ui_LoginForm
from UI.Code.setup_ui import Ui_SetupForm
from UI.Code.wallet_ui import Ui_MainWindow

# %% import the neccessary PyQT GUI utilities
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QSize 

# %% import dependant utilities
import os
import sys
import Encrypter
import Decrypter

# %% 
class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        loggedIn = self.login()
        
        if not loggedIn:
            self.login()
        
        if self.correctPassword:
            self.setupUi(self)

        saved = False
        saved = self.pushButton.clicked.connect(lambda: self.storeData(saved))  # save button
        self.pushButton_3.clicked.connect(self.viewURL)     # view button


    def isPasswordAvalilable(self, path) -> bool:
        '''
        Checks if the password file is availabe
        '''
        return os.path.exists(path)
    
    def login(self) -> QDialog:
        '''
        First checks if the password file is available 
        * if it is not available the it loads up 
        * the setup form
        otherwise it loads up the login form 
        '''
        # Check if the person is logging in or setting up
        # the account 
        loggingIn = False  # Checks if a user has logged in 
        finished = False
        
        
        if self.isPasswordAvalilable('.Data/.encryptedPassword'):
            # Loads the Login Form
            loggingIn = True
            loadLogin = QDialog()
            window  = Ui_LoginForm(loadLogin)
            data = Decrypter.getData('.Data/.passwordKey', '.Data/.encryptedPassword')
            window.header.setText((data["username"]).title())
            window.Login.clicked.connect(lambda: self.getData(window, loggingIn, loadLogin))
            loadLogin.show()
            loadLogin.exec_()
            return True
        else:
            # Loads the Setup Form
            loadSetup = QDialog()
            window = Ui_SetupForm(loadSetup) 
            window.Setup.clicked.connect(lambda: self.getData(window, loggingIn, loadSetup))
            loadSetup.show()
            loadSetup.exec_()
            return False
        
    def getData(self, window, loggingIn, dialog):
        '''
        Gets the inputed data from the form 
        * if the user was setting up his account then the 
        * data will be encrypted then stored 
        * else: 
        * if the user was logging in then it will firsst of all 
        * verify the user
        '''
        if loggingIn:   # checks if the user is in the SetupForm or the Login Form
            data = Decrypter.getData('.Data/.passwordKey', '.Data/.encryptedPassword')
            Password = window.Password.text()
            if data["password"] == Password:
                self.correctPassword = True
            else:
                self.correctPassword = False
        else:
            password = window.Password.text()
            username = window.Username.text()
            data = {
                'username': username,
                'password': password
            }
            Encrypter.Encrypt(data, '.Data/.passwordKey', '.Data/.encryptedPassword')
            loggingIn = True
        dialog.close()

    def setupMainWindow(self):
        self.setupUi(self)
         # view button
    
    def viewURL(self):
        url = self.URL.text()
        self.webView.load(QUrl(url))
        self.dockWidget.setMinimumSize(QSize(432, 116))
        print(url)
        
        
         
    
    def mainWindowData(self):
        data = {
            "title": self.self.Title.text(),
            "email": self.Email.text(),
            "password": self.Password.text(),
            "url": self.URL.text(),
            "message" : self.Message.text()
        }
        print(data)
        return data
    
    def storeData(self, saved):
        # Chec if the file to store the data is present 
        isFilePresent = self.isPasswordAvalilable(".Data/.encrypted")
        if not saved:       # This prevents data from being saved more than once
            if isFilePresent :
                decryptedData = Decrypter.getData()
                decryptedData.append(self.mainWindowData())
                Encrypter.Encrypt(decryptedData)
            else: 
                data = mainWindowData()
                dataList = [data]
                Encrypter.Encrypt(dataList)
            return True
        else:
            print("The data is already saved")
    





# %%.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sam = MainApplication()
    sam.show()
    sys.exit(app.exec_())

# %%
