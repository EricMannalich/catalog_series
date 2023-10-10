from django.db import models
from simple_history.models import HistoricalRecords
from tinymce.models import HTMLField


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
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'

class Menu(BaseModel):
    TIPO = (
        ('LISTAR', 'Listar'),
        ('INFO', 'Información'),
        ('USER', 'Administracion')
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
        verbose_name = 'Menu'
        verbose_name_plural = 'Menuses'
        #ordering = ('orden',)

    def __str__(self):
        return self.nombre

class Filtro(BaseModel):
    TIPO = (
        ('LISTAR', 'Listar'),
        ('ORDENAR', 'Ordenar'),
        ('TRANSMISION', 'Transmision'),
        ('AUTOCOMPLETAR', 'Autocompletar'),
        ('FECHA', 'Fecha'),
        ('PUNTUACION', 'Puntuacion')
    )
    
    nombre = models.CharField(max_length=80, unique=True,db_index=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=80, unique=True,db_index=True)
    image = models.ImageField(upload_to='icons/', max_length=255, default="none.png")
    localStorageKey = models.CharField(max_length=80, unique=True,db_index=True)
    clasificacion = models.CharField(max_length=16, choices=TIPO, default='LISTAR')
    

    class Meta:
        verbose_name = 'Filtro'
        verbose_name_plural = 'Filtros'
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
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologias'
        ordering = ('orden',)

    def __str__(self):
        return self.nombre