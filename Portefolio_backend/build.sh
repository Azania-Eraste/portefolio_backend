#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Collecter les fichiers statiques (CSS Admin, etc.)
python manage.py collectstatic --no-input

# Appliquer les migrations à la base de données
python manage.py migrate
# Lancer le serveur
python manage.py runserver