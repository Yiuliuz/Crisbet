import os
from os import getcwd,listdir
from datetime import datetime

class OS():
    def __init__(self):
        self.ruta_armando_venta="{}\\data\\ventas\\armando".format(getcwd())
        self.ruta_marchada_venta="{}\\data\\ventas\\marchando".format(getcwd())
        self.ruta_retirada_venta="{}\\data\\ventas\\retirados".format(getcwd())
    def cls(self):
        os.system("cls")
    def copiar_archivo(self,archivo_origen,archivo_destino):
        os.system("copy {} {}".format(archivo_origen,archivo_destino))
    def crear_carpeta(self,ruta):
        os.system("mkdir {}".format(ruta))
    def eliminar_carpeta(self,ruta):
        os.system("rmdir /Q /S {}".format(ruta))
    def eliminar_archivo(self,ruta):
        os.system("erase /Q {}".format(ruta))
    def obtener_dia(self):
        dia=datetime.today().strftime("%d")
        return dia
    def obtener_fecha_numeros(self):
        fecha=datetime.today().strftime("%Y-%m-%d")
        return fecha
    def obtener_fecha_letras(self):
        fecha=datetime.today().strftime("%A, %B %d, %Y")
        return fecha
    def obtener_hora(self):
        hora=datetime.today().strftime("%H:%M:%S")
        return hora