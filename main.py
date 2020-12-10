# -*- coding: utf-8 -*-
import requests
import locale
import re
from lxml import html

import math
import Saver


HOME_URL = ["https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=500&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=300&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Casas&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=5&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Casas&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=3&pagfinal=24&paginicial=0&Mosaico=0&scl=0"]


NUEVO_LINK = ["https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=500&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=300&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Casas&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=5&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Casas&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=3&pagfinal=24&paginicial=0&Mosaico=0&scl=0"]



XPATH_HREF_UNIDADES = '//tr/td/a[@class="tituloresult"]/@href'

XPATH_PRECIO = '//h2[@class="ar15gris"]/b/text()'

XPATH_TITULO1 = '//h2[@class="ar15gris"]/text()'

XPATH_UBICACION = '//table[@class="ar13gris"]//text()'


XPATH_DESCRIPCION = '//div[@id="infocompleta"]/text()'


XPATH_MAPA = '//div[@id="divMapa"]/@onclick'
XPATH_ULTIMA_PAGINA = '//span[@class="ar13naranja"]/text()'

REGEX_UNIDADES = '(?:"url":")(https://.*?)(?:"})'

REGEX_ULTIMA_PAGINA = "(?:-.* )(\d{1,3},?\d?\d?\d?\d?)"
REGEX_LOCATION = "(?:LatitudGM=)(.*?)(?:&LongitudGM=)(.*?)(?:')"
REGEX_LINK = '(?://)(.*?)(?:/)'
REGEX_SOURCE = "(?:www.)(.*?)(?:.com)"
REGEX_PRECIO = "\d.*,?"

def parse_home():
    try:
        indice_url = 0
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        for url in HOME_URL:

            link = re.findall(REGEX_LINK, url)
            source = re.findall(REGEX_SOURCE, url)
            response = requests.get(url)
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            ultima_pagina = (parsed.xpath(XPATH_ULTIMA_PAGINA)[0])
            last_page = int(locale.atof((re.findall(REGEX_ULTIMA_PAGINA, ultima_pagina))[0]))
            cantidad_paginas = math.ceil(last_page / 24)





            indice_pagina = 1


            while cantidad_paginas >= indice_pagina:
                contador = 1
                sigiente_pagina = NUEVO_LINK[indice_url].format(indice_pagina)
                response3 = requests.get(sigiente_pagina)
                notice3 = response3.content.decode('utf-8')
                parsed3 = html.fromstring(notice3)
                unidades_href = parsed3.xpath(XPATH_HREF_UNIDADES)



                for elemento in unidades_href:
                    response2 = requests.get(elemento)
                    notice2 = response2.content.decode('utf-8')
                    parsed2 = html.fromstring(notice2)

                    objeto_mapa = parsed2.xpath(XPATH_MAPA)
                    if len(objeto_mapa) > 0:
                        mapa = re.search(REGEX_LOCATION, objeto_mapa[0])
                        latitud = mapa.group(1)
                        longitud = mapa.group(2)
                    else:
                        latitud = "Null"
                        longitud = "Null"

                    precio = re.findall(REGEX_PRECIO, (parsed2.xpath(XPATH_PRECIO)[1]))
                    ubicacion = parsed2.xpath(XPATH_UBICACION)

                    zona = parsed2.xpath(XPATH_TITULO1)[0] + parsed2.xpath(XPATH_PRECIO)[0].strip()
                    colonia = parsed2.xpath(XPATH_TITULO1)[1].strip() + ' ' + ubicacion[3].strip()
                    title = zona + ' ' + colonia

                    description = parsed2.xpath(XPATH_DESCRIPCION)[0].strip()

                    if indice_url == 0 or indice_url== 2:
                        land = "Null"
                        construccion = "Null"
                    else:
                        land = ubicacion[7].strip()
                        construccion = ubicacion[6].strip()


                    dictionary = {
                        "Price": precio,
                        "Location": ubicacion[1].strip(),
                        "Latitude": latitud.strip(),
                        "Longitude":longitud.strip(),
                        "Link": link,
                        "Title": title.strip(),
                        "Description": description.strip(),
                        "Square Meter Land": land,
                        "Square Meter Construction": construccion,
                        "Bathroom": ubicacion[5].strip(),
                        "Bedroom": ubicacion[4].strip(),
                        "Source": source

                    }

                    file_name = "Inmobiliarias.csv"
                    instancia_saver = Saver.Saver(file_name)
                    instancia_saver.crear_csv(dictionary)

                    print("nuevo href")
                    contador += 1
                    print(contador)
                indice_pagina += 1

            indice_url += 1







    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    parse_home()