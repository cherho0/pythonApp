import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.137.220', 8009))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

     # 发送数据:
s.sendall(b'a')
time.sleep(2)
s.sendall(b'd')
time.sleep(2)
s.sendall(b'w')
time.sleep(2)
s.sendall(b's')
time.sleep(2)
    

str=''
while str!='quit':
    print(s.recv(1024).decode('utf-8'))
    
