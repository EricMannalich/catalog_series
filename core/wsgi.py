"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

PROYECT_NAME = os.environ.get('PROYECT_NAME', default="core")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROYECT_NAME + '.settings')

application = get_wsgi_application()
