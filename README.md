Bonjour à tous,

Je suis le formateur pour la session Python qui commence ce vendredi.
Les supports seront disponibles sur
https://gitlab.univ-rennes1.fr/pnavaro/osur-python-2017/ Le projet
n’est pas public car ce n’est pas autorisé sur ce serveur. Je dois
vous ajouter un par un. J’ai déjà trouvé plusieurs d’entre vous.
Il vous suffit de vous connecter une fois avec votre identifiant
sesame et je pourrais vous  ajouter comme membre avant vendredi.

Pour les personnes n'ayant pas de distribution python sur leur
poste, je leur recommande d’installer Miniconda avec Python 3.6
(https://conda.io/miniconda.html)

Voici les commandes pour récupérer les supports

```bash
$ git config --global user.name “Prenom Nom"
$ git config --global user.email “prenom.nom@univ-rennes1.fr"
$ git clone https://gitlab.univ-rennes1.fr/pnavaro/osur-python-2017.git
```

Sur les postes windows, vous pouvez installer git avec la commande 
```bash
$ conda install git
```
tapée dans le anaconda prompt.

Actuellement le dépôt est vide mais dès le début de la formation
vous pourrez télécharger les supports avec la commande

```bash
$ cd osur-python-2017
$ git pull
```

Des corrections et mises à jour seront certainement nécessaires
pendant et après la formation.

Pour installer les packages nécessaires, nous allons créer un
environnement dédié

```bash
$ conda env create -f environment.yml
$ source activate osur2017
```

Pierre
