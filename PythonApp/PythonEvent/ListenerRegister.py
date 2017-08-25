import sys

def data_listener(*events):
    def wapper_f(f):
        f.events=events
        return f
    return wapper_f

class DataEvent(object):
    _events=[]
    def __init__(self, name):
        self.name = name;
        self._callback= []
        DataEvent._events.append(self)

    def __iadd__(self,cb):
        self._callback.append(cb)
        return self

    def __call__(self,*args,**kwargs):
        for cb in self._callback:
            try:
                cb(*args,**kwargs)
            except:
                ex = sys.exc_info()
                print(ex)

    def __repr__(self):
        return 'DATAEVENT %s' % self.name

    @classmethod
    def clear(cls):
        for event in cls._events:
            event._cb = []

    
Onmsg = DataEvent('Onmsg')

onlogin = DataEvent('onlogin')
    
