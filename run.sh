#!/bin/bash
cd /home/ubuntu/catalog_series/
source env/bin/activate
git pull
python3 manage.py migrate --noinput
python3 manage.py serie --import
python3 manage.py collectstatic --noinput
gunicorn -c config/gunicorn/conf.py