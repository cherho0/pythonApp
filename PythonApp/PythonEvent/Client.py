from EventBus import EventBus
from ListenerRegister import *

class Client(EventBus):
    def __init__(self, name):
        super(Client,self).__init__(name)
    
    @data_listener(Onmsg)
    def revcMsg(self,msg):
        print(msg)

    @data_listener(onlogin)
    def login(self,acc):
        print('%s login' % acc )

soclient = Client('nyserver')
    



