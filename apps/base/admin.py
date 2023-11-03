from django.contrib import admin

from apps.base.models import *

class BaseAdmin(admin.ModelAdmin):
    list_display = ("nombre", "url", "descripcion",)
    list_display_links = list_display

class IpAddressAdmin(admin.ModelAdmin):
    list_display = ("ip", "continent_name", "country_name", "state_prov", "city", "organization", "user",)
    list_display_links = list_display
    list_filter = ("continent_name", "country_name", "state_prov", "city", "organization", "user",)
    search_fields = ("ip", "continent_name", "country_name", "state_prov", "city", "organization",)

admin.site.register(Menu, BaseAdmin)
admin.site.register(Filtro, BaseAdmin)
admin.site.register(EndBar, BaseAdmin)
admin.site.register(IpAddress, IpAddressAdmin)