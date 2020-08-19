## Python Class 

Everything is an object in Python, and they are all either instances of classes or instances of metaclasses.


### 1. Class Score

``` python
def scope_test():
    def do_local():
        spam = "local spam"
        print(locals())
        print(globals())

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print(locals())
        print(globals())

    def do_global():
        global spam
        spam = "global spam"
        print(locals())
        print(globals())

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


print(globals())
scope_test()
print("In global scope:", spam)
print(globals())
```

### 2. Class And Instance

``` python
class Animal():
    class_variable = "i am a class variable ,shared by all class instance"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
        print("i am instance variable,access by class instance only")
        self._private_variable = "i am a private variable ,just write like this"

    def instance_func(self):
        print("i am a function of class instance")
        print("self is the class instance")

    @classmethod
    def class_func(cls):
        print("i am a funciton of class")
        print("i need to be decoratored by classmethod")
        print("call by class name")
        print("cls is the class")

    @staticmethod
    def static_func():
        print("i am a static method of class")
        print("just an common function put into class")
        print("call by class name")


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)


c = Dog("Floppy")
print(c.class_variable)
print(c.instance_variable)
c.instance_func()
Dog.class_func()
Dog.static_func()

```

### 3. Meta

* Everything is an object in Python, and they are all either instances of classes or instances of metaclasses.

* As soon as you use the keyword class, Python executes it and creates an OBJECT

``` python
class ObjectCreator(object):
    pass
```
is equal to
``` python
ObjectCreator = type("ObjectCreator", (), {})s
```

* type is the built-in metaclass Python uses.

* classes are objects that can create instances.

* classes are themselves instances. Of metaclasses.


* Metaclasses are deeper magic that 99 % of users should never worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).

### 4. Singleton

``` python
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
```

### 5. UniteTest with Tag

* you want Tag func to your unittest

* so you write a decorator , and a __tag__ to testcase

``` python
import unittest

DefultTag = {"All"}


def tag(*any_tag):

    def wrap(func):
        if not hasattr(func, "__tag__"):
            tags = DefultTag
            tags.update(any_tag)
            setattr(func, "__tag__", tags)
        else:
            getattr(func, "__tag__").update(any_tag)
        return func

    return wrap
```
* then you write a testcase and decorator it with tag

``` python
@tag("V1", "V2")
def test_func(self):
    pass
``` 
* now you want to run all test case with tag V1

``` python
run_tag = {"V1"}


class TestTag(unittest.TestCase):

    @tag("V1")
    def test_create_1(self):
        print("test_create_1")

    @tag("V2")
    def test_create_2(self):
        print("test_create_1")
``` 

* bug, all case include, you have to filter case by tag
* when ?
* at test case runtime ,good
* or at test case creation time
* how ?
* metaclass.
* now define a metaclass
``` python
class Meta(type):
    def __new__(cls, clsname, bases, attrs):
        funcs, cases = filter_test_case(attrs)
        for test_case in cases.values():
            if hasattr(test_case, "__tag__") and len(
                getattr(test_case, "__tag__") & run_tag
            ):
                funcs.update(create_case(test_case))
            else:
                continue
        return super(Meta, cls).__new__(cls, clsname, bases, funcs)
``` 
* ok now put it on your unitest

``` python
class TestCaseWithTag(unittest.TestCase, metaclass=Meta):
    pass
``` 
* patch or  inheritance 

* patch
``` python
unittest.TestCase = TestCaseWithTag
```
* run it again, only test_create_1 include
* perfect!
``` python
run_tag = {"V1"}


class TestTag(unittest.TestCase):

    @tag("V1")
    def test_create_1(self):
        print("test_create_1")

    @tag("V2")
    def test_create_2(self):
        print("test_create_1"
```