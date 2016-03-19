import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "EMSC3032",
    version = "0.0.3",
    author = "Sebastien Allgeyer",
    author_email = "sebastien.allgeyer@anu.edu.au",
    description = ("test"),
    package_data={'ems3032',['data/*.dat']}
    ext_package='ems3032'
    packages=['emsc3032'],
    install_requires=['numpy']
)
