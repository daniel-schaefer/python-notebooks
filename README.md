[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/pnavaro/python-notebooks/master)

This tutorial is made for scientists who want to learn Python and eventually step from Matlab.

Python is a general programming language with many scientific libraries. 
It is optimized to be easy to develop in. The same is not true for Matlab which is 
a domain-specific language.

1. Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)

You can eventually install git with conda after its installation in anaconda prompt.
```
conda install git
git config --global user.name “Prenom Nom"
git config --global user.email “prenom.nom@domaine.fr"
```

2.  Download this repository:

```
git clone https://github.com/pnavaro/python-notebooks.git
```

or download as a [zip file](https://github.com/pnavaro/python-notebooks/archive/master.zip).
    
3. Create a new conda environment:

```
conda env create -f environment.yml
source activate python-navaro  # Linux OS/X
activate python-navaro         # Windows
```

4. If you have an existing installation of Jupyter install the new kernel with:

```
python -m ipykernel install --user --name python-navaro --display-name "Python (navaro)"
```

5. Open notebooks with:

```
cd python-navaro
jupyter notebook
```

Pierre
