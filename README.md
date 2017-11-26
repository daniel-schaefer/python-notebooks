[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/pnavaro/python-notebooks/github)

This tutorial is made for scientists who wants to learn Python and eventually step from Matlab.

Python is a general programming language with many scientific libraries. 
It is optimized to be easy to develop in. The same is not true for Matlab which is 
a domain-specific language.

1.  Download this repository:

        git clone https://github.com/pnavaro/python-notebooks.git

    or download as a [zip file](https://github.com/pnavaro/python-notebooks/archive/master.zip).
    
    Windows users can install git with conda after its installation in anaconda prompt.

        conda install git

2. Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)
3. Create a new conda environment:

        conda env create -f environment.yml
        source activate osur2017  # Linux OS/X
        activate osur2017         # Windows

Open notebooks with:

        nbopen 01.Introduction.ipynb

Pierre
