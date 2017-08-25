import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.137.85', 8009))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
     # 发送数据:
     s.send(data)
    

str=''
while str!='quit':
    print(s.recv(1024).decode('utf-8'))
    
