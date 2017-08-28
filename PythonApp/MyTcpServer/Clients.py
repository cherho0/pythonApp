import socketserver
import sys
from msgfactory import msgfactory

msgfactory = msgfactory()

class MyTcpServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        conn = self.request
        self.name = self.client_address.__str__()
        print( ' connecting  ' + self.name)
        #clientmgr.addClient(self.name,self)
        conn.sendall('welcome connect... connect success'.encode('utf-8'))
        #clientmgr.sendall(self.name+' connected')
        while True:
            try:
                data = conn.recv(1024)
                str = data.decode('utf-8')
                self.recmsg(conn,str)
            except:
                conn.close()
                self.finish()
                print('close '+ self.name)
                ex = sys.exc_info()
                print(ex)
                break
           
    #recvmsg
    def recmsg(self,conn,msg):
        conn.sendall(('recvmsg'+msg).encode('utf-8'))
        msgfactory.msg(msg)


        



class Clients():
    clients=dict()
    def __init__(self):
        self.clients = dict()


    def addClient(self,addr,client):
        self.clients[addr]= client
        print(str(self.clients))

    def getclients(self):
        return self.clients

    def sendall(self,str):
        for k,v in self.clients.items():
            v.request.sendall(str.encode('utf-8'))

clientmgr = Clients()
