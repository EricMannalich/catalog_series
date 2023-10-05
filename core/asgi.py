"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

PROYECT_NAME = os.environ.get('PROYECT_NAME', default="core")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROYECT_NAME + '.settings')

application = get_asgi_application()
