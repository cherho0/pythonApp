import sys

''' 
    a python class demo
'''
class Test():

    #hello world
    def ehco(self):
        print('hello world!')

    def __init__(self,arg):
        self.arg=arg

    def test(self):
        pass

    def ret(self):
        return 1

    def call(self):
        v = self.ret
        print(str(v))