#// Libs
import socket
import colorama

# Server vars
Host = '127.0.0.1'
Port = 5050
BufferSize = 4096

def StartServer(host=Host, port=Port):
    colorama.init()

    #// Server setup
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.bind((host, port))
    Server.listen()

    #// Connection
    Connection, _ = Server.accept()
    with Connection:
        Data = Connection.recv(BufferSize)
        Connection.sendall(Data)

    Server.close()

if __name__ == '__main__':
    StartServer()