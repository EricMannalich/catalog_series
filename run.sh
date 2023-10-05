#!/bin/bash
cd /home/ubuntu/core/
source env/bin/activate
git pull
python3 manage.py migrate
python3 manage.py serie --import
python3 manage.py collectstatic --noinput
gunicorn -c gunicorn_conf.py