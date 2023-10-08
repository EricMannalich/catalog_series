import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.conf import settings
from djqscsv import write_csv

from apps.principal.models import *
from apps.base.models import *
from apps.principal.scraper import *

BD_EXPORT = settings.BD_ROOT
BD_MENU = BD_EXPORT + "/menu.csv"
BD_FILTRO = BD_EXPORT + "/filtro.csv"
BD_ENDBAR = BD_EXPORT + "/endbar.csv"
BD_COLOR = BD_EXPORT + "/color.csv"
BD_GENERO = BD_EXPORT + "/genero.csv"
BD_CATEGORIA = BD_EXPORT + "/categoria.csv"
BD_SERIE = BD_EXPORT + "/serie.csv"


def importMenu():
    Model = Menu
    with open(BD_MENU, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            descripcion = row['descripcion'].strip()
            url = row['url'].strip()
            image = row['image'].strip()
            clasificacion = row['clasificacion'].strip()
            content = row['content'].strip()
            orden = row['orden'].strip()
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.descripcion = descripcion
                    un_obj.url = url
                    un_obj.image = image
                    un_obj.clasificacion = clasificacion
                    un_obj.content = content
                    un_obj.orden = orden
                    un_obj.save()
            else:
                insert = Model(nombre = nombre,descripcion = descripcion,url = url,image = image,clasificacion = clasificacion,content = content,orden = orden)
                insert.save()
        return True
    
def importFiltro():
    Model = Filtro
    with open(BD_FILTRO, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            descripcion = row['descripcion'].strip()
            url = row['url'].strip()
            image = row['image'].strip()
            localStorageKey = row['localStorageKey'].strip()
            clasificacion = row['clasificacion'].strip()
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.descripcion = descripcion
                    un_obj.url = url
                    un_obj.image = image
                    un_obj.localStorageKey = localStorageKey
                    un_obj.clasificacion = clasificacion
                    un_obj.save()
            else:
                insert = Model(nombre = nombre,descripcion = descripcion,url = url,image = image,localStorageKey = localStorageKey,clasificacion = clasificacion)
                insert.save()
        return True

def importEndBar():
    Model = EndBar
    with open(BD_ENDBAR, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            descripcion = row['descripcion'].strip()
            url = row['url'].strip()
            image = row['image'].strip()
            orden = row['orden'].strip()
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.descripcion = descripcion
                    un_obj.url = url
                    un_obj.image = image
                    un_obj.orden = orden
                    un_obj.save()
            else:
                insert = Model(nombre = nombre,descripcion = descripcion,url = url,image = image,orden = orden)
                insert.save()
        return True

def importColor():
    Model = Color
    with open(BD_COLOR, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            descripcion = row['descripcion'].strip()
            image = row['image'].strip()
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.descripcion = descripcion
                    un_obj.image = image
                    un_obj.save()
            else:
                insert = Model(nombre = nombre,descripcion = descripcion,image = image)
                insert.save()
        return True

def importGenero():
    Model = Genero
    with open(BD_GENERO, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            descripcion = row['descripcion'].strip()
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.descripcion = descripcion
                    un_obj.save()
            else:
                insert = Model(nombre = nombre,descripcion = descripcion)
                insert.save()
        return True
    
def importCategoria():
    Model = Categoria
    with open(BD_CATEGORIA, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.save()
            else:
                insert = Model(nombre = nombre)
                insert.save()
        return True
    
def importSerie():
    Model = Serie
    with open(BD_SERIE, "r", encoding="utf-8-sig") as csv_file:
        cur = csv.DictReader(csv_file)
        for row in cur:
            modified_date = row['modifieddate'].strip()
            nombre = row['nombre'].strip()
            if not nombre or not modified_date:
                continue
            sinopsis = row['sinopsis'].strip()
            emision = True if row['emision'].strip() == "True" else False
            image = row['image'].strip()
            fecha_salida = datetime.date(datetime.strptime(row['fechasalida'].strip(), "%Y-%m-%d")) 
            categoria_str = row['categoria__nombre'].strip()
            categoria = Categoria.objects.filter(nombre = categoria_str).first()
            if not categoria:
                continue
            genero_str = row['genero__nombre'].strip()
            genero = Genero.objects.filter(nombre = genero_str).first()
            if not genero:
                continue
            cantidad_episodios = int(row['cantidadepisodios'].strip())
            link_imdb = row['linkimdb'].strip()
            promedio_puntuaciones_imdb = float(row['promedio_puntuaciones_imdb'].strip())
            new_date = datetime.date(datetime.strptime(modified_date, "%Y-%m-%d"))
            un_obj = Model.objects.filter(nombre = nombre).first()
            if un_obj:
                is_genero = Model.objects.filter(nombre = nombre, genero = genero).first()
                if not is_genero:
                    un_obj.genero.add(genero)
                old_date = un_obj.modified_date
                if new_date > old_date:
                    un_obj.nombre = nombre
                    un_obj.sinopsis = sinopsis
                    un_obj.emision = emision
                    un_obj.image = image
                    un_obj.fecha_salida = fecha_salida
                    un_obj.categoria = categoria
                    un_obj.cantidad_episodios = cantidad_episodios
                    un_obj.link_imdb = link_imdb
                    un_obj.promedio_puntuaciones_imdb = promedio_puntuaciones_imdb
                    un_obj.save()
                    #print("update serie " + nombre + " con genero " + genero_str )
            else:
                insert = Model(nombre = nombre,sinopsis = sinopsis,emision = emision,image = image,fecha_salida = fecha_salida,categoria = categoria,cantidad_episodios = cantidad_episodios,link_imdb = link_imdb,promedio_puntuaciones_imdb = promedio_puntuaciones_imdb)
                insert.save()
                insert.genero.add(genero)
                #print("create serie " + nombre + " con genero " + genero_str )
        return True

def exportMenu():
    all_obj = Menu.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'descripcion',
        'url',
        'image',
        'clasificacion',
        'content',
        'orden').order_by('orden')
    if all_obj:
        with open(BD_MENU,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return False

def exportFiltro():
    all_obj = Filtro.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'descripcion',
        'url',
        'image',
        'localStorageKey',
        'clasificacion').order_by('nombre')
    if all_obj:
        with open(BD_FILTRO,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return False

def exportEndBar():
    all_obj = EndBar.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'descripcion',
        'url',
        'image',
        'orden').order_by('orden')
    if all_obj:
        with open(BD_ENDBAR,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return 

def exportColor():
    all_obj = Color.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'descripcion',
        'image').order_by('nombre')
    if all_obj:
        with open(BD_COLOR,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return False

def exportGenero():
    all_obj = Genero.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'descripcion').order_by('nombre')
    if all_obj:
        with open(BD_GENERO,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return False

def exportCategoria():
    all_obj = Categoria.objects.filter(state = True).values(
        'modified_date',
        'nombre').order_by('nombre')
    if all_obj:
        with open(BD_CATEGORIA,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return 

def exportSerie():
    all_obj = Serie.objects.filter(state = True).values(
        'modified_date',
        'nombre',
        'sinopsis',
        'emision',
        'fecha_salida',
        'image',
        'categoria__nombre',
        'genero__nombre',
        'cantidad_episodios',
        'promedio_puntuaciones_imdb',
        'link_imdb').order_by('nombre')
    if all_obj:
        with open(BD_SERIE,'wb') as csv_file:
            write_csv(all_obj, csv_file)
        return True
    return False

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--import', 
            action='store_true',
            help='carga los datos base de las series',
            )
        parser.add_argument(
            '--export', 
            action='store_true',
            help='carga los datos base de las series',
            )
        parser.add_argument(
            '--update', 
            action='store_true',
            help='actualiza las series',
            )
        
        parser.add_argument(
            '--download', 
            action='store_true',
            help='actualiza las series con info online',
            )
    
    def handle(self, *args, **options):
        if options['import']:
            control = "Se" if importMenu() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Menu'))
            control = "Se" if importFiltro() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Filtro'))
            control = "Se" if importEndBar() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo EndBar'))
            control = "Se" if importColor() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Color'))
            control = "Se" if importGenero() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Genero'))
            control = "Se" if importCategoria() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Categoria'))
            control = "Se" if importSerie() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' importo Serie'))


        if options['export']:
            control = "Se" if exportMenu() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Menu'))
            control = "Se" if exportFiltro() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Filtro'))
            control = "Se" if exportEndBar() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto EndBar'))
            control = "Se" if exportColor() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Color'))
            control = "Se" if exportGenero() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Genero'))
            control = "Se" if exportCategoria() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Categoria'))
            control = "Se" if exportSerie() else "No se"
            self.stdout.write(self.style.SUCCESS(control + ' exporto Serie'))
        if options['update']:
            series = Serie.objects.all()
            for serie in series:
                serie.save()
                self.stdout.write(self.style.SUCCESS('Se actualiso la serie: ' + str(serie.nombre)))

        if options['download']:
            update_imdb()