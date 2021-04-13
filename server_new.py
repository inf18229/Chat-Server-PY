import socket
import sys
import re
import ssl
import traceback
from _thread import start_new_thread
from headerMessage import HEADER_SIZE

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
ThreadCount = 0

ssl_version = None
certfile = "./cert/certificate.pem"
keyfile = "./cert/key.pem"
ciphers = None

version_dict = {
    "tlsv1.0" : ssl.PROTOCOL_TLSv1,
    "tlsv1.1" : ssl.PROTOCOL_TLSv1_1,
    "tlsv1.2" : ssl.PROTOCOL_TLSv1_2,
    "sslv23"  : ssl.PROTOCOL_SSLv23,
}

def ssl_wrap_socket(sock, ssl_version=None, keyfile=None, certfile=None, ciphers=None):

    #1. init a context with given version(if any)
    if ssl_version is not None and ssl_version in version_dict:
        #create a new SSL context with specified TLS version
        sslContext = ssl.SSLContext(version_dict[ssl_version])
        if option_test_switch == 1:
            print("ssl_version loaded!! =", ssl_version)
    else:
        #if not specified, default
        sslContext = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        
    if ciphers is not None:
        #if specified, set certain ciphersuite
        sslContext.set_ciphers(ciphers)
        if option_test_switch == 1:
            print("ciphers loaded!! =", ciphers)
    
    #server-side must load certfile and keyfile, so no if-else
    sslContext.load_cert_chain(certfile, keyfile)
    print("ssl loaded!! certfile=", certfile, "keyfile=", keyfile)
    
    try:
        return sslContext.wrap_socket(sock, server_side = True)
    except ssl.SSLError as e:
        print("wrap socket failed!")
        print(traceback.format_exc())


class ChatServer:
    def __init__(self):
        self.server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST,PORT))
        self.server_socket.listen(5)
        self.registeredClient = []
    def getserverSocket(self):
        return self.server_socket
    def recieveData(self,connection):
        while True:
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
        connectionSocket = ssl_wrap_socket(connection,ssl_version,keyfile,certfile,ciphers)
        start_new_thread(MainChatServer.recieveData,(connectionSocket,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

