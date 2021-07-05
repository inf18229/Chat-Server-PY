from headerMessage import format_message,format_register_message, format_login_message, HEADER_SIZE, SIGNAL_SIZE, format_create_chat
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
        uName=input("Username:")
        password = sha256(bytes(getpass("Password:"), 'utf-8')).hexdigest()
        self.client_socket.sendall(bytes(format_login_message(uName, password, 2), 'utf-8'))
        acceptMessageHeader = self.client_socket.recv(HEADER_SIZE)
        if acceptMessageHeader:
            acceptMessageHeader = int(acceptMessageHeader.strip())
            messageSignal = self.client_socket.recv(SIGNAL_SIZE)
            acceptMessage = self.client_socket.recv(acceptMessageHeader)
            if int(messageSignal.strip()) == 32:
                print("Login " + acceptMessage.decode('utf-8'))
                return True
            else:
                print("Login " + acceptMessage.decode('utf-8'))
                return False

    def createChat(self):
        chatPartner_uName = input("Please type the Name of your Chat Partner")
        #TODO: Check if the Chat Partner already exists in local Chat DB
        self.client_socket.sendall(bytes(format_create_chat(chatPartner_uName,3),'utf-8'))
        


    def menue(self):
        return
    def closeConnection(self):
        self.client_socket.close()

if __name__ == "__main__":
    MainChatClient = ChatClient()
    if MainChatClient.registerClient():
        if MainChatClient.loginClient():
            MainChatClient.createChat()
            #MainChatClient.writeMessage()
        else:
            print("Somthing went wrong during login")
    else:
        print("Failure on registering the client")
        MainChatClient.closeConnection()