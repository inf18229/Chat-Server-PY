import socket
from _thread import start_new_thread
from headerMessage import HEADER_SIZE
from server_sql import SQLServer

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
ThreadCount = 0

class ChatServer:
    def __init__(self):
        self.server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST,PORT))
        self.server_socket.listen(5)
        self.registeredClient = []
        self.UserDB = SQLServer()
    def getserverSocket(self):
        return self.server_socket
    def recieveData(self,connection,address):
        while True:
            acceptMessageHeader = connection.recv(HEADER_SIZE)
            if acceptMessageHeader:
                acceptMessageHeader = int(acceptMessageHeader.strip())
                acceptMessage = connection.recv(acceptMessageHeader)
                print(address[0],":",address[1],"-->",acceptMessage.decode('utf-8'))
                self.UserDB.getUserName("StefanM")
    def registerClient(self,connection):
        self.UserDB.createUserinDB("StefanM","Stefan","Maier")
        self.registeredClient.append(connection)
    def getregisteredClients(self):
        return self.registeredClient
    def __del__(self):
        self.server_socket.close()
    
if __name__=="__main__":
    MainChatServer = ChatServer()
    while True:
        print("Warte auf Verbindung")
        connection, address = MainChatServer.getserverSocket().accept()
        MainChatServer.registerClient(connection)
        start_new_thread(MainChatServer.recieveData,(connection,address))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

