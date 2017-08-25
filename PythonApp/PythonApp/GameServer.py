import socket
import time
import threading

def init():
#编写服务器
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(("*",9999));
    server.listen()
    print("accept connect...")

    def receiveMsg(sock,add):
        print(add)
        sock.send(("welcome").encode('utf-8'))
        while True:
            data = sock.recv(1024*10)
            time.sleep(0.01)
            if not data:break
            print(data.decode('utf-8'))
            sock.send((data.decode('utf-8')).encode('utf-8'))

    while True:
        sock,add = server.accept()
        t = threading.Thread(target=receiveMsg,args=(sock,add))
        t.start()


if __name__ == "__main__":
    init()