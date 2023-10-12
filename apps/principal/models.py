from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.users.models import User

# Create your models here.
PUNTUACION = (
        ('0', _('Null')),
        ('1', _('Terrible')),
        ('2', _('Very Low')),
        ('3', _('Low')),
        ('4', _('Below Average')),
        ('5', _('Average')),
        ('6', _('Above Average')),
        ('7', _('High')),
        ('8', _('Very High')),
        ('9', _('Excellent')),
        ('10', _('Exceptional')),
        )

class Genero(BaseModel):
    nombre = models.CharField(max_length=25, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Categoria(BaseModel):
    nombre = models.CharField(max_length=25, unique=True)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
    
class Color(BaseModel):
    nombre = models.CharField(max_length=8, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cards/', max_length=255)
    
    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ('descripcion',)

    def __str__(self):
        return self.nombre

class Serie(BaseModel):
    nombre = models.CharField(max_length=255, unique=True,db_index=True)
    genero = models.ManyToManyField(Genero, blank=True)
    sinopsis = models.TextField(blank=True, null=True, db_index=True)
    emision = models.BooleanField()
    fecha_salida = models.DateField("fechasalida")
    image = models.ImageField(upload_to='portada/%Y/%m/%d/', max_length=255, null=True, blank = True)
    promedio_puntuaciones = models.DecimalField(max_digits=3, decimal_places=1, default = 0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,db_index=True, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,db_index=True, blank=True, null=True)
    cantidad_episodios = models.IntegerField("cantidadepisodios",default = 0)
    link_imdb = models.URLField("linkimdb",blank=True, null=True)
    promedio_puntuaciones_imdb = models.DecimalField("promedio_puntuaciones_imdb",max_digits=3, decimal_places=1, default = 0)

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Series')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        #Color
        cantidad_episodios = self.cantidad_episodios
        color_carta = "grey"
        if cantidad_episodios <= 0:
            color_carta = "grey"
        elif cantidad_episodios <= 7:
            color_carta = "green"
        elif cantidad_episodios <= 15:
            color_carta = "yellow"
        elif cantidad_episodios <= 30:
            color_carta = "orange"
        elif cantidad_episodios <= 55:
            color_carta = "pink"
        elif cantidad_episodios <= 110:
            color_carta = "blue"
        elif cantidad_episodios <= 500:
            color_carta = "purple"
        else:
            color_carta = "black"

        model_color = Color.objects.filter(nombre = color_carta).first()
        if model_color:
            self.color = model_color

        #Puntuacion
        puntuaciones = Puntuacion.objects.filter(serie = self)
        suma_puntuaciones = 0
        for puntuacion in puntuaciones:
            suma_puntuaciones = suma_puntuaciones + int(puntuacion.puntuacion)
        puntuaciones_cont = puntuaciones.count()

        promedio_puntuaciones_imdb = self.promedio_puntuaciones_imdb
        if promedio_puntuaciones_imdb > 0:
            suma_puntuaciones = suma_puntuaciones + promedio_puntuaciones_imdb
            puntuaciones_cont = puntuaciones_cont + 1

        if puntuaciones_cont > 0:
            promedio_puntuaciones = suma_puntuaciones/puntuaciones_cont
        else:
            promedio_puntuaciones = 0
        self.promedio_puntuaciones = promedio_puntuaciones

        #Guardar
        super().save(*args, **kwargs)

class Episodio(BaseModel):
    nombre = models.CharField(max_length=255)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE,db_index=True)
    link = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = _('Episode')
        verbose_name_plural = _('Episodes')

    def __str__(self):
        return self.nombre

class Puntuacion(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    puntuacion = models.CharField(max_length=2, choices=PUNTUACION, default = '0')

    class Meta:
        verbose_name = _('Score')
        verbose_name_plural = _('Scores')

    def __str__(self):
        return '%s %s %s' % (self.usuario, self.serie, self.puntuacion)

    def save(self, *args, **kwargs):
        #Borrar puntuacion anterior
        old_puntuacion = Puntuacion.objects.filter(usuario = self.usuario, serie = self.serie).first()
        if old_puntuacion:
            old_puntuacion.delete()
        super().save(*args, **kwargs)
        #Guardar el prommedio de las puntuaciones de la serie
        puntuaciones = Puntuacion.objects.filter(serie = self.serie)
        suma_puntuaciones = 0
        for puntuacion in puntuaciones:
            suma_puntuaciones = suma_puntuaciones + int(puntuacion.puntuacion)
        puntuaciones_cont = puntuaciones.count()

        serie = Serie.objects.filter(id = self.serie.id).first()
        promedio_puntuaciones_imdb = serie.promedio_puntuaciones_imdb
        if promedio_puntuaciones_imdb > 0:
            suma_puntuaciones = suma_puntuaciones + promedio_puntuaciones_imdb
            puntuaciones_cont = puntuaciones_cont + 1

        if puntuaciones_cont > 0:
            promedio_puntuaciones = suma_puntuaciones/puntuaciones_cont
        else:
            promedio_puntuaciones = 0
        serie.promedio_puntuaciones = promedio_puntuaciones
        serie.save()
