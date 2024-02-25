from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.base.models import *

class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu

class MenuAdmin(ImportExportModelAdmin):
    resource_class = MenuResource
    list_display = ("nombre", "url", "descripcion",)
    list_display_links = list_display

class FiltroResource(resources.ModelResource):
    class Meta:
        model = Filtro

class FiltroAdmin(ImportExportModelAdmin):
    resource_class = FiltroResource
    list_display = ("nombre", "url", "descripcion",)
    list_display_links = list_display

class EndBarResource(resources.ModelResource):
    class Meta:
        model = EndBar

class EndBarAdmin(ImportExportModelAdmin):
    resource_class = EndBarResource
    list_display = ("nombre", "url", "descripcion",)
    list_display_links = list_display
class IpAddressResource(resources.ModelResource):
    class Meta:
        model = IpAddress

class IpAddressAdmin(ImportExportModelAdmin):
    resource_class = IpAddressResource
    list_display = ("ip", "continent_name", "country_name", "state_prov", "city", "organization", "user",)
    list_display_links = list_display
    list_filter = ("continent_name", "country_name", "state_prov", "city", "organization", "user",)
    search_fields = ("ip", "continent_name", "country_name", "state_prov", "city", "organization",)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Filtro, FiltroAdmin)
admin.site.register(EndBar, EndBarAdmin)
admin.site.register(IpAddress, IpAddressAdmin)