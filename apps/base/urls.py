from django.urls import path

from .views import index
from .api import IpAddressGraphicAPIView, IpAddressMapAPIView

urlpatterns = [
    path('', index),
    path('<int:pk>', index),
    path('inicio', index),
    path('about', index),
    path('serie/', index),
    path('serie/<int:pk>', index),
    path('Login', index),
    path('user_admin', index),
    path('ip_address_graphic', index),
    path('frontend/ip_address_graphic/',IpAddressGraphicAPIView.as_view(), name = 'ip_address_graphic'),
    path('frontend/ip_address_map/',IpAddressMapAPIView.as_view(), name = 'ip_address_map'),
]