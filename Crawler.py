import requests
from lxml import html
import re
import locale
import math
import Scraper



XPATH_HREF_UNIDADES = '//tr/td/a[@class="tituloresult"]/@href'
XPATH_ULTIMA_PAGINA = '//span[@class="ar13naranja"]/text()'


REGEX_UNIDADES = '(?:"url":")(https://.*?)(?:"})'

REGEX_ULTIMA_PAGINA = "(?:-.* )(\d{1,3},?\d?\d?\d?\d?)"

REGEX_LINK = '(?://)(.*?)(?:/)'
REGEX_SOURCE = "(?:www.)(.*?)(?:.com)"






class Crawler:
    def __init__(self, url, nuevo_link):
        self.__url = url
        self.__nuevo_link = nuevo_link



    def Crawlear_web(self,url):

        response = requests.get(url)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
        else:
            print("La Pagina no responde")

        return parsed



    def Crawler_Main(self):

        indice_url = 0
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        link = re.findall(REGEX_LINK, self.__url)
        source = re.findall(REGEX_SOURCE, self.__url)
        url = self.__url
        parsed = Crawler.Crawlear_web(self, url)

        ultima_pagina = (parsed.xpath(XPATH_ULTIMA_PAGINA)[0])
        last_page = int(locale.atof((re.findall(REGEX_ULTIMA_PAGINA, ultima_pagina))[0]))  # transforma el string con , como separador de mil en entero
        cantidad_paginas = math.ceil(last_page / 24)

        indice_pagina = 1

        while cantidad_paginas >= indice_pagina:
            contador = 1
            sigiente_pagina = self.__nuevo_link.format(indice_pagina)

            parsed3 = Crawler.Crawlear_web(self, sigiente_pagina)

            unidades_href = parsed3.xpath(XPATH_HREF_UNIDADES)

            for elemento in unidades_href:

                parsed2 = Crawler.Crawlear_web(self, elemento)
                instancia_scraper = Scraper.Scraper()
                instancia_scraper.CrearDicc(parsed2, indice_url, link, source)


                print("nuevo href")
                print(contador)
                contador += 1

            indice_pagina += 1
            print("Cambio de pagina")
        print("Nueva Url")


