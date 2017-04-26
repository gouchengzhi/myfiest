class bbb(object):
    inin=10
    def __init__(self,value):
        self.__value=value
        bbb.inin+=value
        print(bbb.inin)
    def my(self,s):
        print(s)