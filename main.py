# %% imports the UI code 
from UI.Code.login_ui import Ui_LoginForm
from UI.Code.setup_ui import Ui_SetupForm
from UI.Code.wallet_ui import Ui_MainWindow

# %% import the neccessary PyQT GUI utilities
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

# %% import dependant utilities
import os
import Encrypter
import Decrypter

# %% 
class MainApplication(Ui_MainWindow):
    def __init__(self):
        pass

    def isPasswordAvalilable(self) -> bool:
        '''
        Checks if the password file is availabe
        '''
        return os.path.exists('.Data/.password')
    
    def login(self) -> str:
        '''
        First checks if the password file is available 
        * if it is not available the it loads up 
        * the setup form
        otherwise it loads up the login form 
        '''
        if self.isPasswordAvalilable():
            loadLogin = QDialog()
            window  = Ui_LoginForm(loadLogin)
        else:
            loadSetup = QDialog()
            window = Ui_SetupForm(loadSetup)






# %%
