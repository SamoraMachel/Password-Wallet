# %% imports the UI code 
from UI.Code.login_ui import Ui_LoginForm
from UI.Code.setup_ui import Ui_SetupForm
from UI.Code.wallet_ui import Ui_MainWindow
from UI.Code.dataBoard_ui import Ui_Database

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

        self.saved = False
        self.pushButton.clicked.connect(lambda: self.storeData())  # save button
        self.pushButton_3.clicked.connect(self.viewURL)     # view button
        self.pushButton_2.clicked.connect(self.database)    # database button

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
    
    def viewURL(self):
        """
        Open the web browser engine and displays the page 
        requested from the url inserted by the user
        """
        url = self.URL.text()
        self.webView.load(QUrl(url))
        self.dockWidget.setMinimumSize(QSize(418, 116))
         
    def mainWindowData(self) -> dict:
        # gets the data inserted by the user for the MainWindow interface
        data = {
            "title": self.Title.text(),
            "email": self.Email.text(),
            "password": self.Password.text(),
            "message" : self.Message.toPlainText(),
            "url": self.URL.text(),
        }
        return data  
    
    def storeData(self):
        '''
        First checks if the file is saved 
        * If it is not saved : 
            It checks if the file to store the 
            data is present 
            then ...
            it gets the data entered by the user
            get the title and store makes it the 
            key of the data 
        * If it is saved : 
            it gets the data then 
            replaces the existing data with the one entered 
            by the user 
        '''
        # Check if the file to store the data is present 
        isFilePresent = self.isPasswordAvalilable(".Data/.encrypted")
        if not self.saved:       # This prevents data from being saved more than once
            if isFilePresent :
                # saves a file 
                data = self.mainWindowData()
                decryptedData = Decrypter.getData()
                decryptedData[data['title']] = data
                dataToSave = decryptedData
                
            else: 
                data = self.mainWindowData()
                dataList = {data['title']: data}
                dataToSave = dataList  
                self.saved = True
        else :
            data = self.mainWindowData()
            decryptedData = Decrypter.getData()
            decryptedData[data['title']] = data
            dataToSave = decryptedData
        Encrypter.Encrypt(dataToSave)

    def database(self):
        QDatabaseDialog = QDialog()
        Interface = Ui_Database(QDatabaseDialog)
        Interface.table.setRowCount(13)

        try: 
            userData = Decrypter.getData()
            tableRow = 0
            # the amount of items in the database
            itemCount = len(userData)
            if itemCount >  13: # Set the row to equal amount of items
                Interface.table.setRowCount(itemCount)

            for item in userData:
                databaseKey = userData[item]
                Interface.table.setItem(tableRow, 0, QTableWidgetItem(databaseKey['title']))
                Interface.table.setItem(tableRow, 1, QTableWidgetItem(databaseKey['email']))
                Interface.table.setItem(tableRow, 2, QTableWidgetItem(databaseKey['password']))
                Interface.table.setItem(tableRow, 3, QTableWidgetItem(databaseKey['message']))
                tableRow += 1
        except Exception as E:
            QMessageBox.information(self, "Information", f"{E}")
            

        QDatabaseDialog.show()
        QDatabaseDialog.exec_()
        


# %% 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sam = MainApplication()
    sam.show()
    sys.exit(app.exec_())

# %%
