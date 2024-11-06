from setuptools import setup, find_packages

setup(
    name             = 'my_package_name',
    version          = '1.0.0',
    description      = 'Test package for distribution',
    author           = 'standing-o',
    author_email     = 'osyoung540@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],   # AUTO INATALLATION
	include_package_data=True,
	packages=find_packages(),
    keywords         = [],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 