import socket,threading
from headerMessage import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class ChatServer:
    def __init__(self):
        self.server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST,PORT))
        self.server_socket.listen()
    def getserverSocket(self):
        return self.server_socket
    def recieveData(self,connection):
        while True:
            acceptMessageHeader = connection.recv(HEADER_SIZE)
            if acceptMessageHeader:
                acceptMessageHeader = int(acceptMessageHeader.strip())
                acceptMessage = connection.recv(acceptMessageHeader)
                print(acceptMessage.decode('utf-8'))
    
if __name__=="__main__":
    MainChatServer = ChatServer()
    while True:
        connection, address = MainChatServer.getserverSocket().accept()
        print("Verbindung akzpetiert")
        #chatThread = threading.Thread(target=MainChatServer.recieveData(connection))
        #chatThread.start()
        #chatThread.join()
        MainChatServer.recieveData(connection)

