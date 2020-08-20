
# module is just a python file

from dep import Variable

print(f"{__file__}:{__name__}")

if __name__ == "__main__":
    print(Variable)

NewValue = 2

load_module = __import__("dep")
print(getattr(load_module, "Variable"))
setattr(load_module, "Variable", NewValue)
print(getattr(load_module, "Variable"))
