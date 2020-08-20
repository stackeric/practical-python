## Python Module 

Module is a single Python file
Package is a directory of Python modules containing an additional \_\_init\_\_.py file


### 1. Package&Module
```shell
modules
├── README.md
├── \_\_init\_\_.py
├── \_\_main\_\_.py
├── dep.py
└── main.py
```

* directory modules is a package
* dep.py is a module
  
### 2. \_\_init\_\_.py

* when import module
* \_\_init\_\_.py will be executed

### 3. \_\_main\_\_.py

* when run module by python -m modules
* \_\_main\_\_.py will be executed



### 4. if \_\_name\_\_ == "\_\_main\_\_"

* when python run module
* module's \_\_name\_\_ is \_\_main\_\_
* when import moduel
* module's \_\_name\_\_ is module's name
  
### 5. \_\_import\_\_

* load module by module file name

``` python

load_module = __import__("dep")
print(getattr(load_module, "Variable"))
setattr(load_module, "Variable", NewValue)
print(getattr(load_module, "Variable")

``` 

### 6. what happens when you import a module

* When an import statement is executed, the standard builtin __import__() function is called

### 7. structure for a Python application

* Doesn't too much matter. Whatever makes you happy will work

```shell
|- LICENSE
|- README.md
|- TODO.md
|- docs
|   |-- conf.py
|   |-- generated
|   |-- index.rst
|   |-- installation.rst
|   |-- modules.rst
|   |-- quickstart.rst
|   |-- sandman.rst
|- requirements.txt
|- sandman
|   |-- __init__.py
|   |-- exception.py
|   |-- model.py
|   |-- sandman.py
|   |-- test
|       |-- models.py
|       |-- test_sandman.py
|- setup.py
```