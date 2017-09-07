import threading
import time
import http.client
#"http://localhost:801/"
def maxget(times,url,port,para):
    for i in range(0,times):
        t = threading.Thread(target=get(url,port,para))
        t.start()
        t.join()

def get(url,port,para):
    conn = http.client.HTTPConnection(url,port)
    conn.request("GET", '/',para)
    r = conn.getresponse()
    #print(r.getheaders())
    print(r.status)    
    conn.close()

if __name__ == "__main__":
    maxget(100,"localhost",801,'')
