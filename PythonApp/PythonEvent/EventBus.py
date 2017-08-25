import inspect
from ListenerRegister import DataEvent

'''
    event demo for listen
'''

class EventBus(object):
    def __init__(self, name):
        self.busname = name
        self.init_event_linstens()

    def init_event_linstens(self):
        for listen_name,listener in inspect.getmembers(self,lambda f: hasattr(f,"events")):
            for event in listener.events:
                event+=listener

    def destory(self):
        print('clear')
    




