# -*- coding: utf-8 -*-

import Crawler

HOME_URL = ["https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=500&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=300&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Casas&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=5&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Casas&PlazaBusqueda=2&Plaza=2&pagina=1&idinmueble=3&pagfinal=24&paginicial=0&Mosaico=0&scl=0"]


NUEVO_LINK = ["https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=500&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Departamentos&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=300&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Renta-Casas&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=5&pagfinal=24&paginicial=0&Mosaico=0&scl=0",
            "https://www.avisosdeocasion.com/Resultados-Inmuebles.aspx?n=Venta-Casas&PlazaBusqueda=2&Plaza=2&pagina={}&idinmueble=3&pagfinal=24&paginicial=0&Mosaico=0&scl=0"]




def parse_home():
    try:
        indice_link = 0
        for url in HOME_URL:
            instancia_crawler_main = Crawler.Crawler(url, NUEVO_LINK[indice_link])
            instancia_crawler_main.Crawler_Main()
            indice_link += 1





    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    parse_home()