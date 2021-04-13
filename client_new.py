from headerMessage import format_message
from socket import *
import sys
import re
import ssl
import pprint
import traceback

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server


class ChatClient:
    def __init__(self):
        self.client_socket = socket(AF_INET,SOCK_STREAM)
        try:
            sslContext = ssl.create_default_context()
            sslContext.check_hostname = False
            sslContext.verify_mode = ssl.CERT_NONE
            sslContext.load_default_certs()
            self.client_socket = sslContext.wrap_socket(self.client_socket)
        except ssl.SSLError:
            print("wrap socket failed!")
            print(traceback.format_exc())
            sock.close()
            sys.exit(-1)
        self.client_socket.connect((HOST, PORT))
    def writeMessage(self):
        while True:
            nachricht = input("Nachricht\n")
            self.client_socket.send(bytes(format_message(nachricht),'utf-8'))

if __name__ == "__main__":
    MainChatClient = ChatClient()
    MainChatClient.writeMessage()