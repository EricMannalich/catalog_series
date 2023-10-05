#!/bin/bash
cd /home/ubuntu/core/
source env/bin/activate
git pull
python3 manage.py serie --export
