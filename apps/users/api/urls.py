from django.urls import include, path

from apps.users.api.api import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    #path('login/',Login.as_view(), name = 'login'),
    #path('logout/',Logout.as_view(), name = 'logout'),
]