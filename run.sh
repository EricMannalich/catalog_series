#!/bin/bash
cd /home/ubuntu/catalog_series/
git pull
source env/bin/activate
python manage.py migrate --noinput
python manage.py serie --import
python manage.py collectstatic --noinput
deactivate
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo service nginx restart