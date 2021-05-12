# Module and Package
- Resuable tools in python
- It is in a single file with ".py" file extension, and several modules are managed in a "Package"
- 
## Basic structure of python project
```
ROOT
├── setup.py
└── algorithms
   ├── __init__.py
   ├── array.py
└── tests   
   ├── __init__.py
   └── test_array.py
```
- If "__init__.py" file exists in the directory, it is considered a package.
- It uses a module called ```array```, which is being tested from a package called ```algorithms```.

### test_array.py | [[Code]]()
- ```from [package_name] import [module_name]```  
-> Use modules from packages


### algorithms/__init__.py | [[Code]]()
- When a package is referenced from outside, the "__init__.py" in the package is executed.

### setup.py | [[Code]]()
- Determine the top-level directory of the project with ```setup.py```
- Contains information necessary for testing, building, and deployment of the project.
-> [Using the ```setuptools``` package](https://packaging.python.org/tutorials/packaging-projects/#setup-args).
- Install required packages in execution environment of the project  
``` $ python setup.py install```
- Build and Test the project ("Build" : Packaging steps for publishing the repository, not Compiling)  
``` $ python setup.py build```  
``` $ python setup.py test```


