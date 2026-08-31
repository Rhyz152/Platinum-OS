#// Libs
import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QPushButton)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Client.ClientSocket import LoginAttempt as SendLoginAttempt

#// MainWindow
class MWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.InitUi()

    def InitUi(self):
        self.setWindowTitle('Platinum VM 🩶')
        self.setGeometry(150, 200, 1500, 800)

        # Label setup
        self.GreetLabel = QLabel('  Platinum VM 🩶', self)
        self.GreetLabel.setGeometry(600, 100, 400, 100)
        self.GreetLabel.setObjectName('GreetL')

        #// Login interface setup
        self.NameInput = QLineEdit(self)
        self.NameInput.setPlaceholderText('Enter username')
        self.NameInput.setGeometry(600, 250, 400, 100)
        self.PasswordInput = QLineEdit(self)
        self.PasswordInput.setPlaceholderText('Enter password')
        self.PasswordInput.setGeometry(600, 350, 400, 100)
        self.LoginButton = QPushButton(self)
        self.LoginButton.setText('Login')
        self.LoginButton.setGeometry(600, 500, 400, 100)
        self.LoginButton.clicked.connect(self.LoginAttempt)

        # Style
        self.setStyleSheet("""
        QMainWindow{
            background-color: black;
        }
        QLineEdit{
            color: white;
            background-color: #3b3b3b;
            font-size: 30px;
        }
        QPushButton{
            color: white;
            background-color: #474747;
            font-size: 45px;
            border: 5px;
            border-radius: 10px
        }
        QLabel{
            color: white;
            font-size: 50px;
        }
        """)

    def LoginAttempt(self):
        Username = self.NameInput.text()
        Password = self.PasswordInput.text()
        print(f'Attempt to login with: {Username}')

        Response = SendLoginAttempt(Username, Password)
        print(f'Server replied: {Response.decode(encoding="utf-8", errors="replace")}')
        
if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainWindow = MWindow()
    MainWindow.show()
    sys.exit(App.exec_())