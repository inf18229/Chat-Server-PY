import socket,threading
from headerMessage import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class ChatServer:
    def __init__(self):
        self.server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST,PORT))
        self.server_socket.listen()
        self.registeredClient = []
    def getserverSocket(self):
        return self.server_socket
    def recieveData(self,connection):
        acceptMessageHeader = connection.recv(HEADER_SIZE)
        if acceptMessageHeader:
            acceptMessageHeader = int(acceptMessageHeader.strip())
            acceptMessage = connection.recv(acceptMessageHeader)
            print(acceptMessage.decode('utf-8'))
    def registerClient(self,connection):
        self.registeredClient.append(connection)
    def getregisteredClients(self):
        return self.registeredClient
    
if __name__=="__main__":
    MainChatServer = ChatServer()
    while True:
        print("Warte auf Verbindung")
        connection, address = MainChatServer.getserverSocket().accept()
        #MainChatServer.registerClient(connection
        print("Verbindung akzpetiert")
        while True:
            ChatThread = threading.Thread(target=MainChatServer.recieveData(connection),daemon=True)
            ChatThread.start()
            print("Thread startet")
            ChatThread.join()
            break
            #MainChatServer.recieveData(connection)

