import os
from decouple import config
from django.conf import settings
from django.urls.conf import re_path
from django.views.static import serve

URLPATTERNS = [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]

IS_STATIC_SERVER = bool(int(os.environ.get('IS_STATIC_SERVER', default=config('IS_STATIC_SERVER', default='1'))))


URL_STATIC_SERVER = URLPATTERNS if IS_STATIC_SERVER else []
