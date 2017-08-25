import socketserver

class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall('test')
        while True:
            data = conn.recv(1024)