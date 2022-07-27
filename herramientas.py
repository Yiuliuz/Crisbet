import os
import subprocess
import getpass
from os import getcwd,listdir
from datetime import datetime
from traceback import format_exc


"""
CLASES PRIMARIAS (SE DEBEN DECLARAR OBJETOS DE CADA CUAL)
"""
class Data:
    def __init__(self):
        self.ruta_temporales="{}\\data\\temp".format(getcwd())
        self.ruta_locales="{}\\data\\local".format(getcwd())
        self.rutas={
            "r2":"{}\\r2".format(self.ruta_temporales),
            "oculta":"{}\\cesar\\elvago".format(self.ruta_locales)}
        #Crear consultor de db
        self.consultor=Consultor()
        self.consultor.iniciar_codificador(self.obtener_secuencia())
        #-
    def cambiar_vbs(self,nombre):
        with self.consultor.leer_archivo_fijo("{}\\vbs\\{}.txt".format(self.ruta_locales,nombre)) as vbs:
            self.crear_archivo_plano("{}\\auxil.vbs".format(self.ruta_temporales),vbs)
    def obtener_secuencia(self):
        secuencia=self.consultor.leer_archivo_plano("{}\\secuencia.txt".format(self.rutas["oculta"])).split("\n")
        abc=str()
        for caracter in secuencia:
            abc=abc+chr(int(caracter))
        return abc
class Sistema:
    def copiar_arbol(self,ruta_origen,ruta_destino):
        os.system("xcopy /E /C{} {}".format(ruta_origen,ruta_destino))
    def copiar_archivo(self,archivo_origen,archivo_destino):
        os.system("copy {} {}".format(archivo_origen,archivo_destino))
    def crear_carpeta(self,ruta):
        os.system("mkdir {}".format(ruta))
    def eliminar_carpeta(self,ruta):
        os.system("rmdir /Q /S {}".format(ruta))
    def eliminar_archivo(self,ruta):
        os.system("erase /Q {}".format(ruta))
    def ejecutar(self,nombre):
        data.cambiar_vbs(nombre)
        subprocess.run("{}\\auxil.vbs".format(data.ruta_temporales),shell=True)
        self.eliminar_archivo("{}\\auxil.vbs".format(data.ruta_temporales))
class Tiempo:
    def __init__(self):
        pass
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
        now=datetime.now()
        hora=now.strftime("%H:%M:%S")
        return hora
    def obtener_numero_de_turno(self):
        hora=datetime.today().strftime("%H")
        if int(hora) << 16:
            return "1"
        else:
            return "2"
class Cesar:
    def __init__(self):
        self.data=Data_Cesar()
    def comprobar_cuenta(self,usuario,contraseña):
        acceso=False
        nombre="None"
        privilegios=0
        for cuenta in self.data.accounts:
            acc=cuenta.split(",")
            if acc[0]==usuario:
                if acc[1]==contraseña:
                    acceso=True
                    nombre=acc[0]
                    privilegios=int(acc[2])
                else:
                    pass
            else:
                pass
        return [acceso,nombre,privilegios]
class UI:
    def __init__(self):
        self.visual=Visual()
        self.data=Data_UI()
    def index(self):
        while True:
            self.visual.cls()
            self.visual.menu("MENÚ PRINCIPAL - HERRAMIENTAS",["Crear Producto"])
            selection=self.visual.prompt()
            if selection=="0":
                break
            elif selection=="1":
                r1=self.crear_producto()
                while True:
                    if r1=="logout":
                        break
                    else:
                        try:
                            exec("{}".format(self.data.obtener_r2()))
                            r1=self.data.obtener_r2()
                        except ValueError:
                            self.visual.error_selection(format_exc)
                            break
            elif selection=="2":
                pass
            else:
                pass
    def crear_producto(self):
        while True:
            self.visual.cls()
            self.visual.menu[""]
"""
CLASES SECUNDARIAS (NO HAY QUE DECLARARLAS, SON DECLARADAS Y UTILIZADAS POR LAS CLASES PRIMARIAS)
"""
class Visual:
    def __init__(self):
        self.separador="________________________________________________________________________________"
        self.separador_centro="                    ________________________________________                    "
    def cls(self):
        os.system("cls")
    def prompt(self,nombre="UserUnknown"):
        print(self.separador_centro)
        print(self.espaciado(nombre.capitalize(),80))
        print(self.separador_centro)
        p=self.espaciado("♦ ",80)
        x=input(p[2:])
        return x
    def error_selection(self,exc):
        self.cls()
        print("")
        print("                     HA OCURRIDO UN ERROR DE PROCEDIMIENTO")
        print("                    ========================================                    ")
        print("")
        print(exc)
        print("")
        input()
    def espaciado(self,texto,ancho):
        resultado=str()
        renglones=texto.split("\n")
        espacios=int(ancho)-len(renglones[0])
        for renglon in renglones:
            x=0
            while x<=espacios/2:
                resultado=resultado+" "
                x=x+1
            resultado=resultado+renglon+"\n"
        return resultado[:-1]
    def menu(self,titulo,opciones):
        print("")
        print(self.separador_centro)
        print(self.espaciado(titulo,80))
        print(self.separador_centro)
        print("")
        print("                    ----------------------------------------")
        x=1
        for opcion in opciones:
            print("                       {}    |   {}".format(x,opcion))
            print("                    ----------------------------------------")
            x=x+1
        print("                   |   0    |   Volver     ♦     Cancelar   |")
        print("                    ----------------------------------------")
    def titulo(self,titulo):
        print("")
        print(self.separador_centro)
        print(self.espaciado(titulo.upper(),80))
        print(self.separador_centro)
    def confirmar(self):
        print(self.separador_centro)
        print(self.espaciado("CONFIRMAR?",80))
        print(self.separador_centro)
        print("                    ----------------------------------------")
        print("                   |   1    |   Si                          |")
        print("                    ----------------------------------------")
        print("                   |   2    |   No (Volver ♦ Cancelar)      |")
        print("                    ----------------------------------------")
class Codificador:
    def __init__(self,secuencia):
        self.clave_fija=13
        self.clave_turno=int(tiempo.obtener_dia())
        self.secuencia=secuencia
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
class Consultor:
    def __init__(self):
        pass
    def iniciar_codificador(self,secuencia):
        self.codificador=Codificador(secuencia)
    def crear_archivo_plano(self,ruta,texto):
        with open(ruta,"w") as txt:
            txt.write(str(texto))
            txt.close()
    def leer_archivo_plano(self,ruta):
        with open(ruta,"r") as txt:
            texto=txt.read()
            txt.close()
        return texto
    def crear_archivo_turno(self,ruta,texto):
        with open(ruta,"w") as txt:
            txt.write(self.codificador.chr_ascii(self.codificador.encriptar(str(texto),self.codificador.clave_turno)))
            txt.close()
    def leer_archivo_turno(self,ruta):
        with open(ruta,"r") as txt:
            texto=txt.read()
            txt.close()
        return self.codificador.desencriptar(self.codificador.ascii_chr(texto),self.codificador.clave_turno)
    def crear_archivo_fijo(self,ruta,texto):
        with open(ruta,"w") as txt:
            txt.write(self.codificador.chr_ascii(self.codificador.encriptar(str(texto),self.codificador.clave_fija)))
            txt.close()
    def leer_archivo_fijo(self,ruta):
        with open(ruta,"r") as txt:
            texto=txt.read()
            txt.close()
        return self.codificador.desencriptar(self.codificador.ascii_chr(texto),self.codificador.clave_fija)    
"""
CLASES HEREDADAS (SON CLASES ESPECIFICAS PARA CADA OCACSION)
"""
class Data_UI(Data):
    def __init__(self):
        super().__init__()
    def cambiar_r2(self,texto):
        self.consultor.crear_archivo_turno("{}\\index.txt".format(self.rutas["r2"]),texto)
    def obtener_r2(self,programa):
        return self.consultor.leer_archivo_turno("{}\\index.txt".format(self.rutas["r2"]))
class Data_Cesar(Data):
    def __init__(self):
        super().__init__()
        self.accounts=self.consultor.leer_archivo_fijo("{}\\accounts.txt".format(self.rutas["oculta"])).split("\n")
        self.secuencia=super().obtener_secuencia()
        self.clave_fija=13
        self.clave_turno=int(tiempo.obtener_dia())
class Data_Nuevo_Producto(Data):
    def __init__(self):
        super.__init__()
        self.diagrama={
            
        }

"""
DECLARACIONES
"""
sistema=Sistema()
tiempo=Tiempo()
data=Data()
cesar=Cesar()
interfaz=UI()

interfaz.index()
