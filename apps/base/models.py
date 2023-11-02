from django.db import models
from simple_history.models import HistoricalRecords
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField(default = True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    modified_date = models.DateField("modifieddate",auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(user_model="users.User", inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = _('Base Model')
        verbose_name_plural = _('Base Models')

class Menu(BaseModel):
    TIPO = (
        ('LISTAR', _('List')),
        ('INFO', _('Information')),
        ('USER', _('Administration'))
    )
    nombre = models.CharField(max_length=80, unique=True,db_index=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=80, unique=True,db_index=True)
    image = models.ImageField(upload_to='icons/', max_length=255, default="none.png")
    image_body = models.ImageField("image_body",upload_to='body/', max_length=255, default="none.png")
    clasificacion = models.CharField(max_length=16, choices=TIPO, default='LISTAR')
    content = HTMLField(blank=True, null=True)
    orden = models.IntegerField(default = 0)

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        #ordering = ('orden',)

    def __str__(self):
        return self.nombre

class Filtro(BaseModel):
    TIPO = (
        ('LISTAR', _('List')),
        ('ORDENAR', _('Order')),
        ('TRANSMISION', _('Transmission')),
        ('AUTOCOMPLETAR', _('Autocomplete')),
        ('FECHA', _('Date')),
        ('PUNTUACION', _('PuntuacionScore'))
    )
    
    nombre = models.CharField(max_length=80, unique=True,db_index=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=80, unique=True,db_index=True)
    image = models.ImageField(upload_to='icons/', max_length=255, default="none.png")
    localStorageKey = models.CharField(max_length=80, unique=True,db_index=True)
    clasificacion = models.CharField(max_length=16, choices=TIPO, default='LISTAR')
    

    class Meta:
        verbose_name = _('Filter')
        verbose_name_plural = _('Filters')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class EndBar(BaseModel):
    nombre = models.CharField(max_length=80, unique=True,db_index=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=80, unique=True,db_index=True)
    image = models.ImageField(upload_to='endbar/', max_length=255, default="none.png")
    orden = models.IntegerField(default = 0)

    class Meta:
        verbose_name = _('Technology')
        verbose_name_plural = _('Technologies')
        ordering = ('orden',)

    def __str__(self):
        return self.nombre
    
class IpAddress(BaseModel):
    ip = models.CharField(max_length=39, unique=True,db_index=True)
    continent_code = models.CharField(max_length=2, blank=True, null=True)
    continent_name = models.CharField(max_length=16, blank=True, null=True)
    country_code2 = models.CharField(max_length=2, blank=True, null=True)
    country_code3 = models.CharField(max_length=3, blank=True, null=True)
    country_name = models.CharField(max_length=64, blank=True, null=True)
    state_prov = models.CharField(max_length=64, blank=True, null=True)
    state_code = models.CharField(max_length=16, blank=True, null=True)
    district = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)
    latitude = models.CharField(max_length=16, blank=True, null=True)
    longitude = models.CharField(max_length=16, blank=True, null=True)
    calling_code = models.CharField(max_length=5, blank=True, null=True)
    country_flag = models.CharField(max_length=64, blank=True, null=True)
    organization = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('User Info IP')
        verbose_name_plural = _('Users Info IP')
        ordering = ('ip',)

    def __str__(self):
        return self.ip