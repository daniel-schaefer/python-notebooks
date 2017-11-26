Bonjour à tous,

Je suis le formateur pour la session Python qui commence ce vendredi.
Pour les personnes n'ayant pas de distribution python sur leur
poste, je leur recommande d’installer Miniconda avec Python 3.6
(https://conda.io/miniconda.html). Les utilisateurs windows auront besoin de
Microsoft Visual Studio.

Voici les commandes pour récupérer les supports

```bash
$ git clone https://github.com/pnavaro/python-notebooks.git
```

Sur les postes windows, vous pouvez installer git avec la commande 
```bash
$ conda install git
```
tapée dans le anaconda prompt.

Pour installer les packages nécessaires, nous allons créer un
environnement dédié

```bash
$ conda env create -f environment.yml
$ source activate osur2017
$ activate osur207 #(windows)
```

Pierre
