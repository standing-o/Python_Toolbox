# Module and Package
- Resuable tools in python
- It is in a single file with ".py" file extension, and several modules are managed in a "Package"

## 1. Basic structure of python project
```
ROOT
├── setup.py
├── requirements.txt
└── algorithms
   ├── __init__.py
   ├── array.py
└── tests   
   ├── __init__.py
   └── test_array.py
```
- If ```__init__.py``` exists in the directory, it is considered a package.
- It uses a module called ```array```, which is being tested from a package called ```algorithms```.

### test_array.py
- ```from [package_name] import [module_name]```  
-> Use modules from packages


### algorithms/__init__.py
- When a package is referenced from outside, the ```__init__.py``` in the package is executed.
- Each directory in the package must have ```__init__.py```. 
- ```__init__.py``` may be empty or may provide information about the modules contained in the package.

### setup.py
- Determine the top-level directory of the project with ```setup.py```
- Contains information necessary for testing, building, and deployment of the project.
-> [Using the ```setuptools``` package](https://packaging.python.org/tutorials/packaging-projects/#setup-args).
- Install required packages in execution environment of the project  
``` $ python setup.py install```
- Build and Test the project ("Build" : Packaging steps for publishing the repository, not Compiling)  
``` $ python setup.py build```  
``` $ python setup.py test```

## 2. Pip
- Downloading packages from PyPI and integrating them into the project.  
1. Pip version check  
``` $ pip --version ```  
2. Update  
``` $ pip install -U pip``` # On Linux or OS X  
``` $ python -m pip install -U pip```  # On Windows  
3. Install the package registered in PyPI, Python Package Index  
``` $ pip install requests```  
``` $ pip install requests==2.18.0```  
4. Install the package using Requirements Files  
``` $ pip install -r requirements.txt```  
- Summary  
```
$ python
$ python hello_world.py
$ python -m unittest
$ python -m unittest tests/test_array.py
$ python setup.py install
$ python setup.py test
$ pip install [package_name]
$ pip install -U [package_name]
$ pip install -U requirements.txt
$ pip install -U -r requirements.txt
```

## References
```
[1] 파이썬 프로젝트의 구조, https://www.holaxprogramming.com/2017/06/28/python-project-structures/
```
