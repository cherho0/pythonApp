import socketserver
from che import che
che = che()
class msgfactory(object):
    msgdict = dict()

    def __init__(self):
        w = wmsg('w')
        self.msgdict['w'] = w
        s = wmsg('s')
        self.msgdict['s'] = s
        a = wmsg('a')
        self.msgdict['a'] = a
        d = wmsg('d')
        self.msgdict['d'] = d


    def msg(self,msg):
        if msg in self.msgdict:
            self.msgdict[msg].onmsg(msg)
        else:
            print(msg)



class msgbase(object):
    def __init__(self,cmd):
        self.cmd = cmd

    def onmsg(self,msg):
        pass

    def prt(self):
        pass

#w qianjin
class wmsg(msgbase):
    def __init__(self,cmd):
        super(wmsg,self).__init__(cmd)
    
    def onmsg(self,msg):
        print(msg)
        che.qianjin(0.5)
        self.prt()
#s
class smsg(msgbase):
    def __init__(self,cmd):
        super(smsg,self).__init__(cmd)
    
    def onmsg(self,msg):
        print(msg)
        che.cabk(0.5)
#a
class amsg(msgbase):
    def __init__(self,cmd):
        super(amsg,self).__init__(cmd)
    
    def onmsg(self,msg):
        print(msg)
        che.left(0.5)
#d
class dmsg(msgbase):
    def __init__(self,cmd):
        super(dmsg,self).__init__(cmd)
    
    def onmsg(self,msg):
        print(msg)
        che.right(0.5)