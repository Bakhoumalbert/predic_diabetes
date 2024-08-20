# predic_diabetes

## Création de l'environnement virtuel et activation de l'environnement virtuel

- pip -m venv myenv
- ./myenv/Script/activate

## Installation des package avec requirements.txt

pandas
numpy
scikit-learn
fastapi
uvicorn

- installation : pip -r install requirements.txt

## Liaison de notre environnement virtuel avec notre github

- git config --global user.name "Bakhoumalbert"
- git config --global user.email "bakhoum.alou21@gmail.com"

## Création du fichier gitignore pour ignorer notre variable d'environnement

- touch .gitignore

## Nous allons pousser les modifications dans notre dépôt git

- git add .
- git status #pour voir le status d
- git commit -m "first commit"
- git push

## Définission de notre app avec Fast API

Pour exécuter une application avec fastapi, on utilise uvicorn

## Dockerisation

Configuration de notre dockerfile

## Configuration du dépoiement avec Procfile

## Lien entre github et github action
