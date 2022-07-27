import os
import subprocess
from os import getcwd,listdir
from datetime import datetime
from traceback import format_exc

# Crisbet beta 

###CLASES DEL BACKEND
class OS():
    def __init__(self):
        self.ruta_temporales="{}\\data\\temp".format(getcwd())
        self.ruta_locales="{}\\data\\local".format(getcwd())
    def copiar_arbol(self,ruta_origen,ruta_destino):
        os.system("xcopy /E {} {}".format(ruta_origen,ruta_destino))
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
    def obtener_numero_de_turno(self):
        hora=datetime.today().strftime("%H")
        if int(hora) << 16:
            return "1"
        else:
            return "2"
    def ejecutar(self,nombre):
        escritor.cambiar_vbs(nombre)
        subprocess.run("{}\\auxil.vbs".format(self.ruta_temporales),shell=True)
        self.eliminar_archivo("{}\\auxil.vbs".format(self.ruta_temporales))
class Escritor_Lector():
    def __init__(self):
        self.ruta_r2="{}\\r2".format(operative_sist.ruta_temporales)
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
    def iniciar_turno(self):
        while True:
            visual.cls()
            print("")
            print("                                 Inicio de caja:")
            inicio=visual.prompt(cajero.nombre_cajero.capitalize())
            visual.cls()
            print("")
            print("                          Inicio ${} - Confirmar?".format(inicio))
            print("                    ========================================                    ")
            print("                   | Opcion |          Descripcion          |")
            print("                    ----------------------------------------")
            print("                   |   1    |   Si                          |")
            print("                    ----------------------------------------")
            print("                   |   2    |   No                          |")
            print("                    ----------------------------------------")
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                break
            else:
                pass
        self.crear_archivo_turno("{}\\cajero.txt".format(cajero.ruta_turno_info),"{},{}".format(cajero.nombre_cajero,cajero.nivel_privilegio)) 
        self.crear_archivo_turno("{}\\inicio.txt".format(cajero.ruta_turno_info),inicio)
        self.crear_archivo_turno("{}\\total.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\efvolocal.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\efvopya.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\efvototal.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\pagoon.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\mp.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\pagado.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_turno("{}\\fiado.txt".format(cajero.ruta_turno_info),0)
        self.crear_archivo_fijo("{}\\key.txt".format(cajero.ruta_turno_info),cesar.clave_turno)
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
        self.crear_archivo_turno("{}\\index.txt".format(self.ruta_r2),texto)
    def obtener_r2(self):
        return self.leer_archivo_turno("{}\\index.txt".format(self.ruta_r2))
    def cambiar_vbs(self,nombre):
        ###AHREEEEEEE?
        self.crear_archivo_plano("{}\\auxil.vbs".format(operative_sist.ruta_temporales),self.leer_archivo_fijo("{}\\data\\local\\vbs\\{}.txt".format(getcwd(),nombre)))
class Cesar():
    def __init__(self):
        self.ruta_locales="{}\\data\\local\\cesar".format(getcwd())
        self.ruta_temporales="{}\\data\\temp\\cesar".format(getcwd())
        self.ruta_oculta="{}\\elvago".format(self.ruta_locales)
        self.secuencia=self.obtener_secuencia_DB()
        self.clave_fija=self.obtener_clave_fija_DB()
        self.clave_turno=int()
    def crear_clave_turno(self):
        self.clave_turno=int(operative_sist.obtener_dia())
    def obtener_secuencia_DB(self):
        secuencia=escritor.leer_archivo_plano("{}\\secuencia.txt".format(self.ruta_oculta)).split("\n")
        abc=str()
        for caracter in secuencia:
            abc=abc+chr(int(caracter))
        return abc
    def obtener_clave_fija_DB(self):
        return int(escritor.leer_archivo_plano("{}\\key.txt".format(self.ruta_oculta)))
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
    def comprobar_cuenta(self,usuario,contraseña):
        cuentas=escritor.leer_archivo_fijo("{}\\accounts.txt".format(self.ruta_oculta)).split("\n")
        acceso=False
        nombre="None"
        privilegios=0
        for cuenta in cuentas:
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
###DECLARACIÓN DE AGENTES DEL BACKEND(el orden es importante)
operative_sist=OS()
escritor=Escritor_Lector()
cesar=Cesar()

###CLASES DEL FRONTEND
class Visual():
    def __init__(self):
        self.ruta="{}\\data\\local\\visual".format(getcwd())
        self.ruta_banners="{}\\banners".format(self.ruta)
        ####################################################
        self.banner_turno=str()
    def cls(self):
        os.system("cls")
    def prompt(self,nombre="UserUnknown"):
        return input("                    ♦ {}> ".format(nombre.capitalize()))
    def error_selection(self):
        self.cls()
        print("")
        print("                    HA OCURRIDO UN ERROR DE PROCEDIMIENTO")
        print("")
        print(exc)
        print("")
        input()
class Cajero():
    def __init__(self):
        self.nombre_cajero=str()
        self.nivel_privilegio=int()
    def iniciar_turno(self):
        if len(listdir("{}\\turno".format(operative_sist.ruta_temporales))) >> 0:
            self.continuar_turno()
        else:
            self.numero_de_turno=str(operative_sist.obtener_numero_de_turno())
            self.nombre_de_turno="{}_turno{}".format(operative_sist.obtener_fecha_numeros(),self.numero_de_turno)
            self.ruta_turno="{}\\turno\\{}".format(operative_sist.ruta_temporales,self.nombre_de_turno)
            self.ruta_turno_info="{}\\info".format(self.ruta_turno)
            self.ruta_retirados="{}\\retirados".format(self.ruta_turno)
            self.ruta_armando="{}\\armando".format(self.ruta_turno)
            self.ruta_marchando="{}\\marchando".format(self.ruta_turno)
            operative_sist.crear_carpeta(self.ruta_turno)
            operative_sist.crear_carpeta(self.ruta_turno_info)
            operative_sist.crear_carpeta(self.ruta_armando)
            operative_sist.crear_carpeta(self.ruta_marchando)
            operative_sist.crear_carpeta(self.ruta_retirados)
            cesar.crear_clave_turno()
            escritor.iniciar_turno()
            visual.banner_turno="   {}            Crisbet - K ♦ - BurgerTown            {}   ".format(self.nombre_de_turno,self.nombre_cajero.capitalize())
    def continuar_turno(self):
        dir=listdir("{}\\turno".format(operative_sist.ruta_temporales))
        self.nombre_de_turno=dir[0]
        self.ruta_turno="{}\\data\\temp\\turno\\{}".format(getcwd(),self.nombre_de_turno)
        self.ruta_retirados="{}\\retirados".format(self.ruta_turno)
        self.ruta_armando="{}\\armando".format(self.ruta_turno)
        self.ruta_marchando="{}\\marchando".format(self.ruta_turno)
        visual.banner_turno="   {}            Crisbet - K ♦ - BurgerTown            {}   ".format(self.nombre_de_turno,self.nombre_cajero)
    def resumen(self):
        pass
    def terminar_turno(self):
        operative_sist.crear_carpeta("{}\\ventas\\{}".format(operative_sist.ruta_locales,self.nombre_de_turno))
        operative_sist.copiar_arbol(self.ruta_turno,"{}\\ventas\\{}\\".format(operative_sist.ruta_locales,self.nombre_de_turno))
        operative_sist.eliminar_carpeta(self.ruta_turno)
###DECLARACION DE AGENTES DEL FRONTEND
visual=Visual()
cajero=Cajero()

def selection1_1_1():
    input("a")
    operative_sist.ejecutar("nuevo_pedido")
    input("")
    return "selection1()"
def selection1_1():
    cajero.iniciar_turno()
    while True:
        visual.cls()
        print("")
        print("————————————————————————————————————————————————————————————————————————————————")
        print(visual.banner_turno)
        print("————————————————————————————————————————————————————————————————————————————————")
        print("")
        print("                                 Turno Iniciado")
        print("                    ========================================                    ")
        print("                   | Opcion |          Descripcion          |")
        print("                    ----------------------------------------")
        print("                   |   1    |   Comenzar nuevo pedido       |")
        print("                    ----------------------------------------")
        print("                   |   2    |   Panel de control            |")
        print("                    ----------------------------------------")
        print("                   |   3    |   Administrador               |")
        print("                    ----------------------------------------")
        print("                   |   4    |   Finalizar Turno             |")
        print("                    ========================================")
        selection=visual.prompt(cajero.nombre_cajero.capitalize())
        if selection=="1":
            escritor.cambiar_r2("selection1_1_1()")
            break
        elif selection=="2":
            pass
        elif selection=="3":
            pass
        elif selection=="4":
            cajero.terminar_turno()
            escritor.cambiar_r2("selection1()")
            break
        else:
            pass
    return 0
def selection1():
    while True:
        visual.cls()
        print("")
        print("                              Bienvenido {}                               ".format(cajero.nombre_cajero.capitalize()))
        print("                    ========================================                    ")
        print("                   | Opcion |          Descripcion          |")
        print("                    ----------------------------------------")
        print("                   |   1    |   Comenzar o Continuar Turno  |")
        print("                    ----------------------------------------")
        print("                   |   2    |   Administrador               |")
        print("                    ----------------------------------------")
        print("                   |   3    |   Finalizar Turno             |")
        print("                    ----------------------------------------")
        print("                   |   4    |   Cerrar Sesión               |")
        print("                    ========================================                    ")
        selection=visual.prompt(cajero.nombre_cajero)
        if selection=="1":
            escritor.cambiar_r2("selection1_1()")
            break
        elif selection=="4":
            escritor.cambiar_r2("logout")
            return "logout"
        else:
            pass
    return 0
def inicio_de_sesion():###interfaz grafica del inicio de sesion
    while True:
        visual.cls()
        print("")
        print("                                    K ♦                                         ")
        print("                                INICIO DE SESION                                ")
        print("                    ========================================                    ")
        usuario=input("                     ♦ Usuario: ")
        contraseña=input("                     ♦ Contraseña: ")
        return cesar.comprobar_cuenta(usuario,contraseña)
def main_loop():
    while True:
        visual.cls()
        print("")
        print("                                    K ♦                                         ")
        print("                             CRISBET - BURGERTOWN                               ")
        print("                    ========================================                    ")
        print("                   | Opcion |          Descripcion          |")
        print("                    ----------------------------------------")
        print("                   |   1    |   Iniciar Sesión              |")
        print("                    ----------------------------------------")
        print("                   |   2    |   Herramientas                |")
        print("                    ----------------------------------------")
        print("                   |   3    |   Salir                       |")
        print("                    ========================================                    ")
        selection=visual.prompt()
        if selection=="1":
            acceso=inicio_de_sesion()
            if acceso[0]==True:
                cajero.nombre_cajero=acceso[1]
                cajero.nivel_privilegio=acceso[2]
                r1=selection1()
                while True:
                    if r1=="logout":
                        break
                    else:
                        try:
                            exec("{}".format(escritor.obtener_r2()))
                            r1=escritor.obtener_r2()
                        except ValueError:
                            visual.error_selection(format_exc())
                            break
            else:
                visual.cls()
                print("")
                input("                      USUARIO Y/O CONTRASEÑA INCORRECTOS")
        elif selection=="2":
            operative_sist.ejecutar("herramientas")
        elif selection=="3":
            visual.cls()
            break
        else:
            pass


main_loop()

