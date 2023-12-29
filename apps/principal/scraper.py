import requests
from bs4 import BeautifulSoup

from apps.principal.models import Serie

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}


def update_imdb():
    series = Serie.objects.all()

    for serie in series:
        URL = serie.link_imdb
        if URL:
            try:
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
            except:
                continue

            item_puntuacion = soup.find("span", attrs={"class": "sc-bde20123-1 cMEQkK"})
            new_puntuacion = 0
            if item_puntuacion :
                new_puntuacion = float(item_puntuacion.get_text())
                if new_puntuacion > 0 and new_puntuacion < 10:
                    serie.promedio_puntuaciones_imdb = new_puntuacion

            item_sinopsis = soup.find("span", attrs={"class": "sc-466bb6c-0 hlbAws"})
            #print({"item_puntuacion":item_puntuacion, "item_sinopsis":item_sinopsis})
            item_sinopsis_text = ""
            if item_sinopsis :
                item_sinopsis_text = item_sinopsis.get_text()
                if len(item_sinopsis_text) > 30:
                    new_item_sinopsis_text = item_sinopsis_text.replace('Read all', '')
                    serie.sinopsis = new_item_sinopsis_text
            serie.save()

            """item_companies = soup.find("li", attrs={"data-testid": "title-details-companies"})
            companies_list = item_companies.find_all("a", attrs={"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"})
            for company in companies_list:
                print("a :",company.get_text())"""
            
            print({"Name":serie.nombre, "Score":new_puntuacion, "Sinopsis_len":len(item_sinopsis_text)})

