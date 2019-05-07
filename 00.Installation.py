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
# # Installation

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## With conda
#
# ### 1. Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 2. Open a terminal (Linux/MacOSX) or a conda prompt (Windows)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 3. Create a new conda environment with python 3.6
#
#
# ```bash
# conda create python=3.6 -n my-env
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 4. Activate the new environment
#
# Activating the conda environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. 
# <pre>
# $ conda activate my-env
# (math-python) $ python
# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> quit()
# </pre>
#
# [Conda envs documentation](https://conda.io/docs/using/envs.html).

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 5. Managing packages with conda
#
# * Use conda-forge channel
# ```sh
# conda config --add channels conda-forge
# ```
#
# * List all packages
# ```sh
# conda list
# ```
#
# * Search a package
# ```sh
# conda search jupyter
# ```
#
# You can also update or remove, check the [documentation](https://conda.io/docs/using/pkgs.html).

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 6. Install jupyter with extensions
#
# ```
# conda install jupyter_contrib_nbextensions
# conda install autopep8
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 7. Enable autopep8 extension
#
# ```
# jupyter nbextension enable code_prettify/autopep8
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## With pip

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 1. First create a [Python environment](https://docs.python.org/3/library/venv.html)
#
# ```dos
# C:\>python -m venv C:\Users\'Username'\my-venv
# C:\Users\'Username'\my-venv\Scripts\activate.bat
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 2. Install pip
#
# ```
# python -m pip install --upgrade pip
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 3. Install jupyter with extensions

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ```
# pip install jupyter_contrib_nbextensions
# jupyter contrib nbextension install --sys-prefix
# pip install autopep8 dataclasses
# jupyter nbextension enable code_prettify/autopep8
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### 4. Managing Packages with pip
#
# - Search a package
#
# ```bash
# pip search lorem
# ```
#
# - Install a package (or update if it is already installed)
#
# ```bash
# pip install -U lorem
# ```
#
# - List packages installed
#
# ```bash
# pip list
# ```
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Get jupyter notebooks
#
#
# ### Clone the repository with git
#
# ```
# conda install git # install with conda if not present
# git config --global user.name “Prenom Nom"
# git config --global user.email “prenom.nom@univ-rennes1.fr"
# git clone https://github.com/pnavaro/python-notebooks.git
# ```
#
# ### Or download zip archive.
#
# https://github.com/pnavaro/python-notebooks/archive/master.zip
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Installing Python Packages from a Jupyter Notebook
#
# ### conda package in the current Jupyter kernel
#
# Example with package `lorem` from *conda-forge*
# ```python
# import sys
# !conda install --yes --prefix {sys.prefix} -c conda-forge lorem
# ```
#
# ### pip package in the current Jupyter kernel
# ```
# import sys
# !{sys.executable} -m pip install lorem
# ```

# %% {"slideshow": {"slide_type": "slide"}}
import sys
print(sys.executable)
