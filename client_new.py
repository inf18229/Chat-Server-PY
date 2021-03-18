from headerMessage import format_message
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

class ChatClient:
    def __init__(self):
        self.client_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
    def writeMessage(self):
        while True:
            nachricht = input("Nachricht\n")
            self.client_socket.sendall(bytes(format_message(nachricht),'utf-8'))

if __name__ == "__main__":
    MainChatClient = ChatClient()
    MainChatClient.writeMessage()