# -*- coding: utf-8 -*-
import requests
import lxml.html as html
import os
import datetime
from bs4 import BeautifulSoup
import re
from lxml import html
import urllib.request
import urllib.parse
from lxml import etree

from io import StringIO, BytesIO
from selenium import webdriver
import time
from selenium.webdriver import chrome
import csv







#import Saver


HOME_URL = "https://www.segundamano.mx/anuncios/nuevo-leon/monterrey/renta-inmuebles/departamentos?orden=date"

XPATH_HREF_UNIDADES = '//a[@class="card-container"]/@href'
XPATH_PRECIO = '//span[@class="av-AdPrice"]/text()'  #(el segundo de la lista es el precio)
XPATH_TITULO = '//h1[@class="av-AdTitle"]/text()' #(el segundo de la lista)
XPATH_UBICACION = '//div[@class="av-AdInformation_Column av-AdInformation-info-loc"]//span/text()' #(SEGUNDO)

XPATH_HABITACIONES = '//span[contains(text(), "Habitaciones")]/../span[2]/text()'
XPATH_BATHROOM = '//span[contains(text(), "Baños")]/../span[2]/text()'
XPATH_SUPERFICIE_TERRENO = '//span[contains(text(), "Superficie de terreno")]/../span[2]/text()'
XPATH_SUPERFICIE = '//span[contains(text(),"Superficie") and not (contains(text(), "terreno"))]/../span[2]/text()'


XPATH_AREA = '//div[@class="detail-lot_area detail-container"]/span/text()' #(SEGUNDO)
XPATH_DESCRIPCION = '//div[@id="ad-description"]/p/text()' #(CONCATENAR LAS LISTAS)


XPATH_CARACTERISTICAS = '//div[@class="av-AdInformation_Column"]//div/span/text()' #(preguntar por Superficie de terreno, Habitaciones, Superficie)


XPATH_ULTIMA_PAGINA = '//a[@class="arrows active"]/@href'
REGEX_UNIDADES = '(?:"url":")(https://.*?)(?:"})'
REGEX_ULTIMA_PAGINA = '(?:Página 1 de )(\d{1,3})'


def parse_home():
    try:

        response = requests.get(HOME_URL)
        content = response.content
        notice = response.content.decode('utf-8')
        parsed = html.fromstring(notice)
        link = response.text
        unidades = re.findall(REGEX_UNIDADES, link)
        # for elemento in unidades:
        #     response2 = requests.get(elemento)
        #     notice2 = response2.content.decode('utf-8')
        #     parsed2 = html.fromstring(notice2)
        #     habitaciones = parsed2.xpath(XPATH_HABITACIONES)
        #     print(habitaciones)



        last_page = re.search(REGEX_ULTIMA_PAGINA, content)



        print(unidades)
        print(last_page)
        # options = webdriver.ChromeOptions()
        # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        # chrome_driver_binary = "/usr/local/bin/chromedriver"
        #
        # C:\Program
        # Files\Google\Chrome\Application
        #
        # driver = webdriver.Chrome(executable_path=r"C:\Users\Yamil\Desktop\chromedriver_win32\chromedriver.exe")
        # driver.get(HOME_URL)
        # time.sleep(2)
        # driver.maximize_window()
        # hasta aqui puede ser un modulo de Crawler que al final devuelve driver
        #
        # href_unidades = driver.find_elements_by_class_name("card-container")
        # print("pene")

        #
        # # today = time.strftime("%d-%m-%Y %H:%M:%S")
        # response = requests.get(HOME_URL)
        # driver.quit()
        # notice = response.content
        # parsed2 = html.fromstring(notice)
        #
        # tree = lxml.html.fromstring(response.text)
        # title_elem = tree.xpath(XPATH_HREF_UNIDADES)
        # title_elem2 = tree.cssselect(XPATH_HREF_UNIDADES)
        # lin = parsed2.xpath(XPATH_HREF_UNIDADES)
        # lin2 = parsed2.cssselect(XPATH_HREF_UNIDADES)
        # print()



    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    parse_home()