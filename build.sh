#!/usr/bin/env bash
# exit on error

# make it executable before pushing 
# chmod +x build.sh


set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate