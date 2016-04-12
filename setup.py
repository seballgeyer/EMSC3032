import os
from setuptools import setup
import inspect
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

SETUP_DIRECTORY = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def find_packages():
    """
    Simple function to find all modules under the current folder.
    """
    modules = []
    for dirpath, _, filenames in os.walk(os.path.join(SETUP_DIRECTORY, "emsc3032")):
        if  "__init__.py" in filenames:
            modules.append(os.path.relpath(dirpath, SETUP_DIRECTORY))
    return [_i.replace(os.sep, ".") for _i in modules]


setup(
    name = "EMSC3032",
    version = "0.0.3",
    author = "Sebastien Allgeyer",
    author_email = "sebastien.allgeyer@anu.edu.au",
    description = ("library for the EMSC3032 lecture ANU"),
    package_data={'emsc3032':['data/*.dat']},
    ext_package='emsc3032',
    packages=['emsc3032'],
    install_requires=['numpy']
)
