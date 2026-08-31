#// Libs
import os, sys, socket, colorama
from PyQt5.QtWidgets import QApplication
from termcolor import colored

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Client.Interface import MainInterface

# Client vars
Host: str = "127.0.0.1"
Port: int = 5050
BufferSize: int = 4096

def LoginAttempt(NameInput: str, PasswordInput: str, host=Host, port=Port) -> bytes:
    colorama.init()
    print(colored(text='[Client]: Sending login attempt', color='cyan'))

    Payload = f"{NameInput}:{PasswordInput}".encode('utf-8')

    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client.connect((host, port))
    Client.sendall(Payload)
    Data = Client.recv(BufferSize)
    Client.close()

    print(colored(text=f'[Client]: Server response: {Data.decode("utf-8", errors="replace")}', color='magenta'))
    return Data

def ConnectClient(host=Host, port=Port) -> bytes:
    colorama.init()
    print(colored(text='[Client]: Connected to server', color='cyan'))

    #// Client setup
    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client.connect((host, port))
    Data = Client.recv(BufferSize)
    Client.close()

    return Data

# Main
if __name__ == '__main__':
    App = QApplication(sys.argv)
    MWindow = MainInterface.MWindow()
    MWindow.show()
    sys.exit(App.exec_())
    ConnectClient()