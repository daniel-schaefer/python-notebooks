# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Modules
#
# If your Python program gets longer, you may want to split it into several files for easier maintenance. To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Run the cell below to create a file named fibo.py with several functions inside:

# %% {"slideshow": {"slide_type": "slide"}}
%%file fibo.py
""" Simple module with
    two functions to compute Fibonacci series """

def fib1(n):
   """ write Fibonacci series up to n """
   a, b = 0, 1
   while b < n:
      print(b, end=', ')
      a, b = b, a+b

def fib2(n):   
    """ return Fibonacci series up to n """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib1(int(sys.argv[1]))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# You can use the function fib by importing fibo which is the name of the file without .py extension.

# %% {"slideshow": {"slide_type": "fragment"}}
import fibo
print(fibo.__name__)
print(fibo.__file__)
fibo.fib1(1000)

# %% {"slideshow": {"slide_type": "slide"}}
help(fibo)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Executing modules as scripts
#
# When you run a Python module with
# ```bash
# $ python fibo.py <arguments>
# ```
# the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". The following code will be executed only in this case and not when it is imported.
# ```python
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
# ```
# In Jupyter notebook, you can run the fibo.py python script using magic command.

# %% {"slideshow": {"slide_type": "slide"}}
%run fibo.py 1000

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# The module is also imported.

# %% {"slideshow": {"slide_type": "fragment"}}
fib1(1000)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Different ways to import a module
# ```python
# import fibo
# import fibo as f
# from fibo import fib1, fib2
# from fibo import *
# ```

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# - Last command with '*' imports all names except those beginning with an underscore (_). In most cases, do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# - If a function with same name is present in different modules imported. Last module function imported replace the previous one.

# %% {"slideshow": {"slide_type": "fragment"}}
from numpy import sqrt
from scipy import sqrt
sqrt(-1)

# %% {"slideshow": {"slide_type": "fragment"}}
from scipy import sqrt
from numpy import sqrt
sqrt(-1)

# %% {"slideshow": {"slide_type": "slide"}}
import numpy as np
import scipy as sp

print(np.sqrt(-1+0j), sp.sqrt(-1))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# - For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter 
# – If you really want to test interactively after a long run, use :
# ```python
# import importlib
# importlib.reload(modulename)
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # The Module Search Path
#
# When a module is imported, the interpreter searches for a file named module.py in a list of directories given by the variable sys.path.
# - Python programs can modify sys.path
# - export the PYTHONPATH environment variable to change it on your system.

# %% {"slideshow": {"slide_type": "fragment"}}
import sys
sys.path

# %% {"slideshow": {"slide_type": "slide"}}
import collections
collections.__path__

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# `sys.path` is a list and you can append some directories:

# %%
sys.path.append("/Users/navaro/python-notebooks/")
print(sys.path)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# When you import a module `foo`, following files are searched in this order:
#
# - **foo.dll**, **foo.dylib** or **foo.so**
# - **foo.py**
# - **foo.pyc**
# - **foo/\_\_init__.py**
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Packages
#
# - A package is a directory containing Python module files.
# - This directory always contains a file name \_\_init\_\_.py

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# <pre>
# marseille
# ├── __init__.py
# ├── calanques
# │   ├── __init__.py
# │   ├── morgiou.py
# │   ├── sorgiou.py
# │   └── sugiton.py
# └── cirm
#     ├── __init__.py
#     ├── annexe.py
#     ├── auditorium.py
#     └── bastide.py
# </pre>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Relative imports
#
# These imports use leading dots to indicate the current and parent packages involved in the relative import. In the sugiton module, you can use:
# ```python
# from . import morgiou # import module in the same directory
# from .. import cirm   # import module in parent directory
# from ..cirm import bastide # import module in another subdirectory of the parent directory
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Reminder
#
# Don't forget that importing * is not recommended

# %% {"slideshow": {"slide_type": "fragment"}}
sum(range(5),-1)

# %% {"slideshow": {"slide_type": "fragment"}}
from numpy import *
sum(range(5),-1)

# %% {"slideshow": {"slide_type": "slide"}}
del sum # delete imported sum function from numpy 
help(sum)

# %% {"slideshow": {"slide_type": "slide"}}
import numpy as np
help(np.sum)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Packaging
#
# To share you package you need to add these following files:
#     
# - `setup.py`
# - `README.rst` or `README.md`
# - `LICENSE`
# - module files
#     
# Optional files:
#     
# - `setup.cfg`
# - `MANIFEST.in`
# - `requirements.txt`
#

# %% [markdown]
# ## Sample repository
#
# ```
# README.md
# LICENSE
# setup.py
# requirements.txt
# package/__init__.py
# package/core.py
# package/helpers.py
# docs/conf.py
# docs/index.rst
# tests/test_basic.py
# tests/test_advanced.py
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Individual tests import context, create a tests/context.py file:
# ```py
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# import package
# ```
#
# Then, within the individual test modules, import the module like so:
# ```py
# from .context import package
# ```
# This will always work as expected, regardless of installation method.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # setup.py 
#
# ```py
# from distutils.core import setup
#
# setup(name='Distutils',
#       version='1.0',
#       description='Python Distribution Utilities',
#       author='Greg Ward',
#       author_email='gward@python.net',
#       url='https://www.python.org/sigs/distutils-sig/',
#       packages=['distutils', 'distutils.command'],
#      )
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Build and install in place
# ```bash
# python setup.py build_ext --inplace
# ```
#
# Install in default Python path
# ```bash
# python setup.py install
# ```

# %% [markdown]
# ```py
# # Author:
# #     Loic Gouarin <loic.gouarin@gmail.com>
# #
# # License: BSD 3 clause
# from setuptools import setup, find_packages
#
# CLASSIFIERS = [
#     "Development Status :: 3 - Alpha",
#     "Intended Audience :: Science/Research",
#     "Intended Audience :: Developers",
#     "License :: OSI Approved :: BSD License",
#     "Programming Language :: Python",
#     "Programming Language :: Python :: 2",
#     "Programming Language :: Python :: 2.7",
#     "Programming Language :: Python :: 3",
#     "Programming Language :: Python :: 3.4",
#     "Programming Language :: Python :: 3.5",
#     "Topic :: Software Development",
#     "Topic :: Scientific/Engineering",
#     "Operating System :: Microsoft :: Windows",
#     "Operating System :: POSIX",
#     "Operating System :: Unix",
#     "Operating System :: MacOS"
# ]
#
# name = "splinart"
#
# MAJOR = 0
# MINOR = 1
# PATCH = 2
# VERSION = "{}.{}.{}".format(MAJOR, MINOR, PATCH)
#
# with open("splinart/version.py", "w") as f:
#     f.write("__version__ = '{}'\n".format(VERSION))
#
# setup(
#     name = "splinart",
#     author = "loic.gouarin@gmail.com",
#     description = "spline art generator",
#     version = VERSION,
#     license = "BSD",
#     classifiers = CLASSIFIERS,
#     packages = find_packages(exclude=["demos"]),
#     install_requires = ["numpy",
#                         "matplotlib>=2",
#                         "six"],
#     entry_points={ 'console_scripts': [
#         'splinart=scripts.cli_splinart:main',
#         ],
#     
# ```

# %%
# %load ../splinart/requirements.txt
numpy
matplotlib
six
pytest
pylint
pytest-pylint
pytest-cov
codecov


# %%

# %%

# %%
