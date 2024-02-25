from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sessions.models import Session
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.users.forms import UserChangeForm, UserCreationForm
from apps.users.models import User as CustomUser

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = CustomUserResource
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_active',)
    list_filter = ( 'is_staff', 'is_active',)
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'image')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','username', 'first_name', 'last_name', )
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Session)
