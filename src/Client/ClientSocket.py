#// Libs
import socket
import colorama
from termcolor import colored

# Client vars
Host: str = "127.0.0.1"
Port: int = 5050
BufferSize: int = 4096

def LoginAttempt(NameInput: str, PasswordInput: str) -> None:
    pass

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
if __name__ == "__main__":
    ConnectClient()