#// Libs
import socket
import colorama
from termcolor import colored

from LoginParse import ParseLoginData, ParseLoginPayload

# Server vars
Host = '127.0.0.1'
Port = 5050
BufferSize = 4096

def ParseIncomingLogin(Data: bytes):
    RawMessage = Data.decode('utf-8', errors='replace')
    print(colored(text=f'[Server]: Raw login data: {RawMessage}', color='yellow'))

    try:
        Username, Password = ParseLoginPayload(RawMessage)
        print(colored(text=f'[Server]: Username = {Username}', color='green'))
        print(colored(text=f'[Server]: Password = {Password}', color='green'))
        return Username, Password
    except ValueError:
        print(colored(text='[Server]: Login payload was not in username:password format', color='red'))
        return '', RawMessage

def StartServer(host=Host, port=Port) -> None:
    colorama.init()
    print(colored(text='[Server]: Started', color='green'))

    #// Server setup
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.bind((host, port))
    Server.listen()

    #// Connection
    Connection, _ = Server.accept()
    with Connection:
        Data = Connection.recv(BufferSize)

        if Data:
            Username, Password = ParseIncomingLogin(Data)
            IsValid = ParseLoginData(Username, Password)

            if IsValid:
                Response = 'Login success'.encode('utf-8')
            else:
                Response = 'Login failed'.encode('utf-8')

            Connection.sendall(Response)
    Server.close()

if __name__ == '__main__':
    StartServer()