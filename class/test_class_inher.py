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
