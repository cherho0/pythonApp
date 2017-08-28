import socketserver
from Clients import *
from msgfactory import msgfactory


if __name__== '__main__':
    addr = '192.168.1.110'
    print('listen in %s' %addr)
    server = socketserver.ThreadingTCPServer((addr,8009),MyTcpServer)
    server.serve_forever()
     
    
    