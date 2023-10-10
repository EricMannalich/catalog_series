import requests
from bs4 import BeautifulSoup

from apps.principal.models import Serie

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}


def update_imdb():
    series = Serie.objects.all()

    for serie in series:
        URL = serie.link_imdb
        if URL:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            item_puntuacion = soup.find("span", attrs={"class": "sc-bde20123-1 iZlgcd"})
            if item_puntuacion :
                serie.promedio_puntuaciones_imdb = float(item_puntuacion.get_text())

            item_sinopsis = soup.find("span", attrs={"class": "sc-466bb6c-2 eVLpWt"})
            if item_sinopsis :
                if len(item_sinopsis > 50):
                    serie.sinopsis = item_sinopsis.get_text()
            serie.save()
            print({"Name":serie.nombre, "Score":item_puntuacion})

