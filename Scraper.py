import re
import Saver

XPATH_PRECIO = '//h2[@class="ar15gris"]/b/text()'
XPATH_TITULO1 = '//h2[@class="ar15gris"]/text()'
XPATH_UBICACION = '//table[@class="ar13gris"]//text()'
XPATH_DESCRIPCION = '//div[@id="infocompleta"]/text()'
XPATH_MAPA = '//div[@id="divMapa"]/@onclick'

REGEX_LOCATION = "(?:LatitudGM=)(.*?)(?:&LongitudGM=)(.*?)(?:')"
REGEX_PRECIO = "\d.*,?"


class Scraper:
    def __init__(self):
        self.__XPATH_MAPA = XPATH_MAPA
        self.__XPATH_PRECIO = XPATH_PRECIO
        self.__XPATH_UBICACION = XPATH_UBICACION
        self.__XPATH_TITULO1 = XPATH_TITULO1
        self.__XPATH_DESCRIPCION = XPATH_DESCRIPCION

    def crear_dicc(self, parsed2, elemento, source, indice_link):

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

        if indice_link%2 == 0:
            land = "Null"
            construccion = "Null"
        else:
            land = ubicacion[7].strip()
            construccion = ubicacion[6].strip()

        dictionary = {
            "Price": precio,
            "Location": ubicacion[1].strip(),
            "Latitude": latitud.strip(),
            "Longitude": longitud.strip(),
            "Link": elemento,
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
