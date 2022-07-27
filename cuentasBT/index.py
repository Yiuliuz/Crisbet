import os
from os import getcwd

class Escritor_Lector():
    def __init__(self):
        self.ruta_r2="r2.txt"
    def chr_ascii(self,texto):
        asc=str()
        renglones=texto.split("\n")
        if len(renglones)==1:
            for caracter in list(renglones[0]):
                asc=asc+str(ord(caracter))+","
        else:
            for renglon in renglones:
                renglon_resultado=str()
                for caracter in list(renglon):
                    renglon_resultado=renglon_resultado+str(ord(caracter))+","
                asc=asc+str(renglon_resultado[:-1])+"-"
        return str(asc[:-1])
    def ascii_chr(self,texto):
        a=str()
        renglones=texto.split("-")
        if len(renglones)==1:
            for caracter in renglones[0].split(","):
                a=a+chr(int(caracter))
        else:
            contador=1
            for renglon in renglones:
                renglon_resultado=str()
                for caracter in renglon.split(","):
                    renglon_resultado=renglon_resultado+chr(int(caracter))
                contador=contador+1
                if contador>>len(renglones):
                    a=a+renglon_resultado
                else:
                    a=a+renglon_resultado+"\n"
        return a
    def crear_archivo_plano(self,ruta,texto):
        txt=open(ruta,"w")
        txt.write(str(texto))
        txt.close()
    def leer_archivo_plano(self,ruta):
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return texto
    def crear_archivo_turno(self,ruta,texto):
        txt=open(ruta,"w")
        txt.write(self.chr_ascii(cesar.encriptar(str(texto),cesar.clave_turno)))
        txt.close()
    def leer_archivo_turno(self,ruta):
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return cesar.desencriptar(self.ascii_chr(texto),cesar.clave_turno)
    def crear_archivo_fijo(self,ruta,texto):
        txt=open(ruta,"w")
        txt.write(self.chr_ascii(cesar.encriptar(str(texto),cesar.clave_fija)))
        txt.close()
    def leer_archivo_fijo(self,ruta):
        clave=cesar.clave_fija
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return cesar.desencriptar(self.ascii_chr(texto),cesar.clave_fija)
    def cambiar_r2(self,texto):
        self.crear_archivo_turno("{}\\pedido.txt".format(self.ruta_r2),texto)
    def obtener_r2(self):
        return self.leer_archivo_turno("{}\\pedido.txt".format(self.ruta_r2))

class Cesar():
    def __init__(self):
        self.secuencia=self.obtener_secuencia_DB()
        self.clave_fija=13
    def obtener_secuencia_DB(self):
        secuencia=escritor.leer_archivo_plano("secuencia.txt").split("\n")
        abc=str()
        for caracter in secuencia:
            abc=abc+chr(int(caracter))
        return abc
    def encriptar(self,plano,clave):
        renglones=plano.split("\n")
        encriptado=str()
        if len(renglones)==1:
            renglon=list(renglones[0])
            for caracter in renglon:
                if caracter  in self.secuencia:
                    indice_caracter=self.secuencia.index(caracter)
                    nuevo_indice=indice_caracter+int(clave)
                    if nuevo_indice>=len(self.secuencia):
                        nuevo_indice=nuevo_indice-len(self.secuencia)
                    else:
                        pass
                    encriptado=encriptado+self.secuencia[nuevo_indice]
                else:
                    encriptado=encriptado+caracter
        else:
            contador=1
            for renglon in renglones:
                renglon_encriptado=str()
                for caracter in list(renglon):
                    if caracter  in self.secuencia:
                        indice_caracter=self.secuencia.index(caracter)
                        nuevo_indice=indice_caracter+int(clave)
                        if nuevo_indice >= len(self.secuencia):
                            nuevo_indice=nuevo_indice-len(self.secuencia)
                        else:
                            pass
                        renglon_encriptado=renglon_encriptado+self.secuencia[nuevo_indice]
                    else:
                        renglon_encriptado=renglon_encriptado+caracter
                contador=contador+1
                if contador>=len(renglones):
                    encriptado=encriptado+renglon_encriptado
                else:
                    encriptado=encriptado+renglon_encriptado+"\n"
        return encriptado
    def desencriptar(self,encriptado,clave):
        renglones=encriptado.split("\n")
        desencriptado=str()
        if len(renglones)==1:
            renglon=list(renglones[0])
            for caracter in renglon:
                if caracter  in self.secuencia:
                    indice_caracter=self.secuencia.index(caracter)
                    nuevo_indice=indice_caracter-int(clave)
                    desencriptado=desencriptado+self.secuencia[nuevo_indice]
                else:
                    desencriptado=desencriptado+caracter
        else:
            contador=1
            for renglon in renglones:
                renglon_desencriptado=str()
                for caracter in list(renglon):
                    if caracter  in self.secuencia:
                        indice_caracter=self.secuencia.index(caracter)
                        nuevo_indice=indice_caracter-int(clave)
                        renglon_desencriptado=renglon_desencriptado+self.secuencia[nuevo_indice]
                    else:
                        renglon_desencriptado=renglon_desencriptado+caracter
                contador=contador+1
                if contador>=len(renglones):
                    desencriptado=desencriptado+renglon_desencriptado
                else:
                    desencriptado=desencriptado+renglon_desencriptado+"\n"
        return desencriptado
class Visual():
    def __init__(self):
        pass
    def cls(self):
        os.system("cls")
    def prompt(self,nombre="UserUnknown"):
        return input("                    ♦ {}> ".format(nombre.capitalize()))
    def error_selection(self,exc):
        self.cls()
        print("")
        print("                     HA OCURRIDO UN ERROR DE PROCEDIMIENTO")
        print("                    ========================================                    ")
        print("")
        print(exc)
        print("")
        input()

escritor=Escritor_Lector()
cesar=Cesar()
visual=Visual()

def main_loop():
    while True:
        visual.cls()
        print("")
        print("                      CREAR CUENTAS BT")
        print("")
        usuario=visual.prompt("Nuevo Usuario")
        print("")
        contraseña=visual.prompt("Nueva Contraseña")
        print("")
        privilegio=visual.prompt("Nivel de Privilegio")
        print("")
        print("                 1. Confirmar   2. Cancelar")
        selection=visual.prompt("Confirmar?")
        if selection=="1":
            escritor.crear_archivo_fijo("{}.txt".format(usuario),"{},{},{}".format(usuario,contraseña,privilegio))
        else:
            pass

main_loop()
    