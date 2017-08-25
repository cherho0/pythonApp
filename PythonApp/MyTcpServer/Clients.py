import socketserver

class MyTcpServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        conn = self.request
        self.name = self.client_address.__str__()
        print( ' 连接了  ' + self.name)
        clientmgr.addClient(self.name,self)
        conn.sendall('测试'.encode('utf-8'))
        clientmgr.sendall(self.name+' connected')
        while True:
            data = conn.recv(1024)
            str = data.decode('utf-8')
            print(str)
            conn.sendall(str.encode('utf-8'))


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
