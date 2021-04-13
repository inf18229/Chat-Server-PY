from headerMessage import format_message
from socket import *
import sys
import re
import ssl
import pprint
import traceback

HOST = "localhost"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

ssl_version = None
certfile = None
keyfile = "./ssl/key.pem"
ciphers = None

version_dict = {
    "tlsv1.0" : ssl.PROTOCOL_TLSv1,
    "tlsv1.1" : ssl.PROTOCOL_TLSv1_1,
    "tlsv1.2" : ssl.PROTOCOL_TLSv1_2,
    "sslv23"  : ssl.PROTOCOL_SSLv23,
}


def ssl_wrap_socket(sock, ssl_version=None, keyfile=None, certfile=None, ciphers=None):
    try:
        #2.init a sslContext with given version (if any)
        if ssl_version is not None and ssl_version in version_dict:
            #create a new SSL context with specified TLS version
            sslContext = ssl.SSLContext(version_dict[ssl_version])
            if option_test_switch == 1:
                print("ssl_version loaded!! =", ssl_version)
        else:
            #default
            sslContext = ssl.create_default_context()
        
        if ciphers is not None:
            #if specified, set certain ciphersuite
            sslContext.set_ciphers(ciphers)
            if option_test_switch == 1:
                print("ciphers loaded!! =", ciphers)
        
        #3. set root certificate path
        if certfile is not None and keyfile is not None:
            #if specified, load speficied certificate file and private key file
            sslContext.verify_mode = ssl.CERT_REQUIRED
            sslContext.check_hostname = True
            sslContext.load_verify_locations(certfile, keyfile)
            if option_test_switch == 1:
                print("ssl loaded!! certfile=", certfile, "keyfile=", keyfile )
            return sslContext.wrap_socket(sock, server_hostname = hostname)
        else:
            #default certs
            sslContext.check_hostname = False
            sslContext.verify_mode = ssl.CERT_NONE
            sslContext.load_default_certs()
            return sslContext.wrap_socket(sock)
        
    except ssl.SSLError:
        print("wrap socket failed!")
        print(traceback.format_exc())
        sock.close()
        sys.exit(-1)


class ChatClient:
    def __init__(self):
        self.client_socket = socket(AF_INET,SOCK_STREAM)
        self.client_socket = ssl_wrap_socket(self.client_socket,ssl_version, keyfile, certfile, ciphers)
        self.client_socket.connect((HOST, PORT))
    def writeMessage(self):
        while True:
            nachricht = input("Nachricht\n")
            self.client_socket.sendall(bytes(format_message(nachricht),'utf-8'))

if __name__ == "__main__":
    MainChatClient = ChatClient()
    MainChatClient.writeMessage()