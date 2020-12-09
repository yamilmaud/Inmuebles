# -*- coding: utf-8 -*-
import requests
import lxml.html as html
import os
import datetime
import Saver


HOME_URL = "https://www.segundamano.mx/anuncios/nuevo-leon/monterrey/renta-inmuebles/departamentos?orden=date"
#
# XPATH_CATEGORIES_NAME = "//div[@class='dropdown category-dropdown']/a/text()"
# XPATH_CATEGORIES_HREF = "//div[@class='dropdown category-dropdown']/a/@href"
# xpath_subtegorias_href = '//div[@arialabelledby="{}"]/a/@href'
# xpath_subtegorias_name ='//div[@arialabelledby="{}"]/a/text()'
#
#
# XPATH_PROD_DETAILS ='//a[@class="btn btn-dark "]/@href'
#
# XPATH_NOMBRE_PRECIO_DESCRIP = '//div[@class="align-self-center"]/h5/text()'
# XPATH_NOMBRE_PRECIO_DESCRIP2 = '//div[@class="align-self-center"]/p/text()'
# XPATH_DESCRIP2 = '//div[@class="card card-outline-secondary my-4 light-box-shadow"]/div/p/text()'





def parse_home():
    try:
        response = requests.get(HOME_URL)
        notice = response.content.decode('utf-8')
        parsed = html.fromstring(notice)


        if response.status_code == 200:

            title = parsed.xpath(XPATH_CATEGORIES_HREF)


            indice = 0
            while indice < len(title):
                indice_subcategoria = 0
                categories_name= parsed.xpath(XPATH_CATEGORIES_NAME)
                nuevolink = title[indice].split('=')[-1]
                xpath_subtegorias2 = xpath_subtegorias_href.format(nuevolink)
                subcategoria = parsed.xpath(xpath_subtegorias2)

                xpath_subcategoria_name2 = xpath_subtegorias_name.format(nuevolink)
                subcategoria_name = parsed.xpath(xpath_subcategoria_name2)




                if len(subcategoria) == 0:
                    nueva_url = HOME_URL + title[indice]
                    response = requests.get(nueva_url)
                    notice = response.content.decode('utf-8')
                    parsed2 = html.fromstring(notice)
                    prod_deatil = parsed2.xpath(XPATH_PROD_DETAILS)

                    for elemento in prod_deatil:
                        nueva_url2 = HOME_URL + elemento
                        response = requests.get(nueva_url2)
                        notice = response.content.decode('windows-1252')
                        parsed3 = html.fromstring(notice)
                        nombre_precio_descip = parsed3.xpath(XPATH_NOMBRE_PRECIO_DESCRIP)
                        nombre_precio_descip2 = parsed3.xpath(XPATH_NOMBRE_PRECIO_DESCRIP2)
                        descrip2 = parsed3.xpath(XPATH_DESCRIP2)



                        if len(nombre_precio_descip2) == 0:
                          nombre_precio_descip2.append("SIN DESCRIPCION")

                        if len(descrip2) == 0:
                            descrip2.append("SIN DESCRIPCION")

                        a_guardar = nombre_precio_descip + nombre_precio_descip2 + descrip2


                        mi_diccionario = {
                            "Categoria": categories_name[indice].strip(),
                            "Marca": categories_name[indice].strip(),
                            "Nombre": a_guardar[0].strip(),
                            "Precio": a_guardar[1].strip(),
                            "Descripcion": a_guardar[2].strip(),
                            "Descripcion adicional": a_guardar[3].strip()
                        }
                        file_name = "EmmaSativa.csv"
                        instancia_saver = Saver.Saver(file_name)
                        instancia_saver.Crear_Csv(mi_diccionario)

                        print(mi_diccionario)



                else:

                    nueva_url = HOME_URL + title[indice]
                    response = requests.get(nueva_url)
                    notice = response.content.decode('utf-8')
                    parsed2 = html.fromstring(notice)



                    for elemento in subcategoria:

                        nueva_url3 = HOME_URL + elemento
                        response = requests.get(nueva_url3)
                        notice = response.content.decode('utf-8')
                        parsed2 = html.fromstring(notice)
                        prod_deatil = parsed2.xpath(XPATH_PROD_DETAILS)

                        for elemento in prod_deatil:
                            nueva_url2 = HOME_URL + elemento
                            response = requests.get(nueva_url2)
                            notice = response.content.decode('windows-1252')
                            parsed3 = html.fromstring(notice)
                            nombre_precio_descip = parsed3.xpath(XPATH_NOMBRE_PRECIO_DESCRIP)
                            nombre_precio_descip2 = parsed3.xpath(XPATH_NOMBRE_PRECIO_DESCRIP2)
                            descrip2 = parsed3.xpath(XPATH_DESCRIP2)

                            if len(nombre_precio_descip2) == 0:
                                nombre_precio_descip2.append("SIN DESCRIPCION")

                            if len(descrip2) == 0:
                                descrip2.append("SIN DESCRIPCION")

                            a_guardar = nombre_precio_descip + nombre_precio_descip2 + descrip2

                            mi_diccionario = {
                                "Categoria": categories_name[indice].strip(),
                                "Marca": subcategoria_name[indice_subcategoria].strip(),
                                "Nombre": a_guardar[0].strip(),
                                "Precio": a_guardar[1].strip(),
                                "Descripcion": a_guardar[2].strip(),
                                "Descripcion adicional": a_guardar[3].strip()
                            }
                            print(mi_diccionario)
                            file_name = "EmmaSativa.csv"
                            instancia_saver = Saver.Saver(file_name)
                            instancia_saver.Crear_Csv(mi_diccionario)

                        indice_subcategoria = indice_subcategoria + 1
                indice += 1


    except ValueError as ve:
        print(ve)



def run():
    parse_home()







if __name__ == '__main__':
    run()

