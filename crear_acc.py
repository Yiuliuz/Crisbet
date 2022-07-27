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

operative_sist=OS()


class Cesar():
    def __init__(self):
        self.ruta_local="{}\\data\\cesar\\local".format(getcwd())
        self.ruta_peticiones="{}\\peticiones".format(self.ruta_local)
        self.ruta_temporales="{}\\data\\cesar\\temp".format(getcwd())
        self.ruta_clave_temporal="{}\\keys".format(self.ruta_temporales)
        self.secuencia=self.obtener_secuencia_DB()
        self.crear_clave_turno()
    def obtener_clave_fija(self):
        assii=escritor.leer_archivo_plano("{}\\key.txt".format(self.ruta_local)).split("\n")
        return len(assii)
    def crear_clave_turno(self):
        self.clave_turno=int(operative_sist.obtener_dia())
        escritor.crear_archivo_plano("{}\\{}.txt".format(self.ruta_clave_temporal,cajero.nombre_de_turno),str(self.clave_turno))
    def obtener_secuencia_DB(self):
        txt=open("{}\\secuencia.txt".format(self.ruta_local),"r")
        secuencia=txt.read().split("\n")
        txt.close()
        abc=str()
        for caracter in secuencia:
            abc=abc+chr(int(caracter))
        return abc
    def encriptar(self,plano,clave):
        renglones=plano.split("\n")
        encriptado=str()
        contador=1
        for renglon in renglones:
            renglon_encriptado=str()
            for caracter in list(renglon):
                if caracter  in self.secuencia:
                    indice_caracter=self.secuencia.index(caracter)
                    nuevo_indice=indice_caracter+int(clave)
                    if nuevo_indice >> len(secuencia):
                        nuevo_indice=nuevo_indice-len(secuencia)
                    else:
                        pass
                    renglon_encriptado=renglon_encriptado+secuencia[nuevo_indice]
                else:
                    renglon_encriptado=renglon_encriptado+caracter
        contador=contador+1
        if contador==len(renglones):
            encriptado=encriptado+renglon_encriptado
        else:
            encriptado=encriptado+renglon_encriptado+"\n"
        return encriptado
    def desencriptar(self,encriptado,clave):
        renglones=encriptado.split("\n")
        desencriptado=str()
        contador=1
        for renglon in renglones:
            renglon_desencriptado=str()
            for caracter in list(renglon):
                if caracter  in self.secuencia:
                    indice_caracter=self.secuencia.index(caracter)
                    nuevo_indice=indice_caracter-int(clave)
                    renglon_desencriptado=renglon_desencriptado+secuencia[nuevo_indice]
                else:
                    renglon_desencriptado=renglon_desencriptado+caracter
        contador=contador+1
        if contador==len(renglones):
            desencriptado=desencriptado+renglon_desencriptado
        else:
            desencriptado=desencriptado+renglon_desencriptado+"\n"
        return desencriptado

cesar=Cesar()
#escritor=Escritor_Lector()

accounts="gonzalo,contraseña,2\nagustin,123456,1\njulio,juliocesar,1"

#escritor.crear_archivo_fijo("{}\data\cesar\local\elvago\accounts.txt".format(getcwd()),accounts)