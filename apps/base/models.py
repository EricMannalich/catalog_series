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