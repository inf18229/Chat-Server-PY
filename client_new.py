from headerMessage import format_message
import socket
import ssl

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

class ChatClient:
    def __init__(self):
        self.context = ""
        self.context = ssl.create_default_context()
        self.context.load_verify_locations('/home/stefanmaier/Dokumente/Privat/cert/server.pem')
        self.client_socket =  socket.create_connection((HOST,PORT))
        self.client_socket = self.context.wrap_socket(self.client_socket, server_hostname=HOST)
    def writeMessage(self):
        while True:
            nachricht = input("Nachricht\n")
            self.client_socket.send(bytes(format_message(nachricht),'utf-8'))

if __name__ == "__main__":
    MainChatClient = ChatClient()
    MainChatClient.writeMessage()