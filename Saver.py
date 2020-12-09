import csv
import os


class Saver:
    def __init__(self, file_name):
        self.__file_name = file_name



    def Crear_Csv(self, valores_diccionario):

        with open('{}'.format(self.__file_name), 'a+', newline='\n') as f:
            writer = csv.DictWriter(f, fieldnames=valores_diccionario.keys())
            if os.stat(self.__file_name).st_size == 0:
                writer.writeheader()

            writer.writerow(valores_diccionario)

