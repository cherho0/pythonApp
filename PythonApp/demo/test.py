import http.client
import threading

def enter(url,port,para,count):
    for i in range(0,count):
        t = threading.Thread(target=get(url,port,para))
        t.start()

def get(url,port,para):
    conn = http.client.HTTPConnection(url,port)
    conn.request('GET','/',para)
    ret = conn.getresponse()
    print(ret.status)

enter('www.baidu.com',80,'',10000)

