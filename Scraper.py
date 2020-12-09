
def CrearDiccionario(self, valores_driver):
    dolar_turista = valores_driver.find_element_by_xpath(self.__XPATH_DOLAR_TURISTA)
    dolar_blue_compra = valores_driver.find_element_by_xpath(self.__XPATH_DOLAR_BLUE_COMPRA)
    dolar_blue_venta = valores_driver.find_element_by_xpath(self.__XPATH_DOLAR_BLUE_VENTA)
    dolar_oficial_compra = valores_driver.find_element_by_xpath(self.__XPATH_DOLAR_OFICIAL_COMPRA)
    dolar_oficial_venta = valores_driver.find_element_by_xpath(self.__XPATH_DOLAR_OFICIAL_VENTA)
    today = time.strftime("%d-%m-%Y %H:%M:%S")

    mi_diccionario = {
        "Fecha": today,
        "Dolar Turista": dolar_turista.text,
        "Dolar Blue Compra": dolar_blue_compra.text,
        "Dolar Blue Venta": dolar_blue_venta.text,
        "Dolar Oficial Compra": dolar_oficial_compra.text,
        "Dolar Oficial Venta": dolar_oficial_venta.text

    }
    return mi_diccionario

