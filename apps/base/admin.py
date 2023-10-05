from django.contrib import admin

from apps.base.models import *

class BaseAdmin(admin.ModelAdmin):
    list_display = ("nombre", "url", "descripcion",)
    list_display_links = list_display

admin.site.register(Menu, BaseAdmin)
admin.site.register(Filtro, BaseAdmin)
admin.site.register(EndBar, BaseAdmin)