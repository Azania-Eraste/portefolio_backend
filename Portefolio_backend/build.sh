#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Collecter les fichiers statiques (CSS Admin, etc.)
python manage.py collectstatic --no-input
