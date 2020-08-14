# 你想通过反省或者重写类定义的某部分来修改它的行为，但是你又不希望使用继 承或元类的方式。

def log_getattribute(cls):
    def new_getattribute(self, name):
        print('getting:', name)
    return orig_getattribute(self, name)
    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
