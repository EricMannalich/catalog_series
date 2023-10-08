#!/bin/bash
cd /home/ubuntu/catalog_series/
git pull
python manage.py migrate --noinput
python manage.py serie --import
python manage.py collectstatic --noinput
gunicorn -c config/gunicorn/conf.py