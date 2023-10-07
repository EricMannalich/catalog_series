@echo off

./env/Scripts/Activate.ps1
git pull
python3 manage.py migrate --noinput
python3 manage.py serie --import
python3 manage.py collectstatic --noinput
python3 manage.py runserver
