
Everything is an object in Python, and they are all either instances of classes or instances of metaclasses.

As soon as you use the keyword class, Python executes it and creates an OBJECT


class ObjectCreator(object):
    pass


is equal to

ObjectCreator = type("ObjectCreator", (), {})

type is the built-in metaclass Python uses.

classes are objects that can create instances.

classes are themselves instances. Of metaclasses.


Metaclasses are deeper magic that 99 % of users should never worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).


import functools


class Singleton(type):

    def __init__(self, *args, **kwargs):
        self.__instance=None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("I am calling")
        if self.__instance == None:
            self.__instance=super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class AClass(metaclass = Singleton):
    def __init__(self, name):
        self.name=name


A1=AClass("x")
print(A1.name)
A2=AClass("y")
print(A2.name)
