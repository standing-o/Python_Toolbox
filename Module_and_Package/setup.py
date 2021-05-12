import io
from setuptools import find_packages, setup

def long_description():
    with io.open('README.rst', 'r', encoding = 'utf-8') ad f:
        readme = f.read()
    return readme

setup(name = 'algorithms',
     version = '0.1',
     description = 'practice python with solving algorithms',
     long_description = long_description(),
     url = 'http://github.com/stunstunstun/awesome-algorithms',
     author = 'stunstunstun',
     author_email = 'agileboys.com@gmail.com',
     license = 'MIT',
     packages = find_packages(),
     classifiers = [
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.6',
     ],
     zip_safe = False)
