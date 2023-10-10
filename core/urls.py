from django.contrib import admin
from django.urls import include, path

from core.static_server import URL_STATIC_SERVER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.routers')),
    path('usuario/', include('apps.users.api.urls')),
    path('principal/', include('apps.principal.api.routers')),
    path('principal/', include('apps.principal.api.urls')),
    path('frontend/', include('apps.base.routers')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('apps.base.urls')),
]

urlpatterns += URL_STATIC_SERVER

admin.site.index_title = "AnimeCards"
admin.site.site_header = "Cards Management"
admin.site.site_title = "Administration"
