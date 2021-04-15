from headerMessage import format_message,format_register_message
from getpass import getpass
from hashlib import sha256
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

class ChatClient:
    def __init__(self):
        self.client_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
    def writeMessage(self):
        while True:
            nachricht = input("Message\n")
            if nachricht=="brake":
                break
            else:
                self.client_socket.sendall(bytes(format_message(nachricht,1),'utf-8'))
    def registerClient(self):
        name = input("Name:")
        surname = input("Surname:")
        uName=input("Username:")
        password = sha256(bytes(getpass("Password:"),'utf-8')).hexdigest()
        verifyPassword = sha256(bytes(getpass("Password:"),'utf-8')).hexdigest()
        if password == verifyPassword:
            self.client_socket.sendall(bytes(format_register_message(name,surname,uName,password,0),'utf-8'))
            return True
        else:
            return False
    def loginClient(self):
        return
    def menue(self):
        return
    def closeConnection(self):
        self.client_socket.close()

if __name__ == "__main__":
    MainChatClient = ChatClient()
    if MainChatClient.registerClient():
        MainChatClient.writeMessage()
    else:
        print("Failure on registering the client")
        MainChatClient.closeConnection()