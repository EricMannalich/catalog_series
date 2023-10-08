from django.urls import path

from .views import index

urlpatterns = [
    path('', index),
    path('<int:pk>', index),
    path('inicio', index),
    path('about', index),
    path('serie/', index),
    path('serie/<int:pk>', index),
    path('Login', index),
    path('user_admin', index),
]