import socketserver
from Clients import *


if __name__== '__main__':
    addr = '127.0.0.1'
    print('listen in %s' %addr)
    server = socketserver.ThreadingTCPServer((addr,8009),MyTcpServer)
    server.serve_forever()
    
    