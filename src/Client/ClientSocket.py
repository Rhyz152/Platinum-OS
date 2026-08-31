#// Libs
import socket

# Client vars
Host = "127.0.0.1"
Port = 5050
BufferSize = 4096

def ConnectClient(host=Host, port=Port):
    #// Client setup
    Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client.connect((host, port))
    data = Client.recv(BufferSize)
    Client.close()



    return data

# Main
if __name__ == "__main__":
    ConnectClient()