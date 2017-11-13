Bonjour à tous,

Je suis le formateur pour la session Python qui commence ce vendredi.
Les supports seront disponibles sur

https://gitlab.univ-rennes1.fr/pnavaro/osur-python-2017/ 

Le projet n’est pas public car ce n’est pas autorisé sur ce serveur. Je dois
vous ajouter un par un. J’ai déjà trouvé plusieurs d’entre vous.
Il vous suffit de vous connecter une fois avec votre identifiant
sesame et je pourrais vous  ajouter comme membre avant vendredi.

Voici les commandes pour récupérer les supports

```bash
git config --global user.name “Prenom Nom"
git config --global user.email “prenom.nom@univ-rennes1.fr"
git clone git@gitlab-ssh.univ-rennes1.fr:pnavaro/osur-python-2017.git
```

Actuellement le dépôt est vide mais dès le début de la formation
vous pourrez télécharger les supports avec la commande

```bash
cd osur-python-2017
git pull
```

Des corrections et mises à jour seront certainement nécessaires
pendant et après la formation.

Pour les personnes qui n’ont pas de distribution python sur leur
poste, je leur recommande d’installer Miniconda avec Python 3.6
(https://conda.io/miniconda.html)

Pour installer les packages nécessaires, nous allons créer un
environement dédié

```bash
conda env create -f environment.yml
source activate osur2017
```

Pierre
