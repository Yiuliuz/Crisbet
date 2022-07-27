import os
import subprocess
from os import getcwd,listdir
from datetime import datetime

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
        subprocess.run("{}\\auxil.vbs".format(self.ruta_temporales,),shell=True)
class Escritor_Lector():
    def __init__(self):
        pass
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
            inicio=visual.prompt()
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
            selection=visual.prompt()
            if selection=="1":
                break
            else:
                pass
        self.crear_archivo_turno("{}\\cajero.txt".format(cajero.ruta_turno_info),cajero.nombre_cajero)
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
        self.crear_archivo_plano("{}\\herramientas\\r2.txt".format(getcwd()),texto)
    def obtener_r2(self):
        return self.leer_archivo_plano("{}\\herramientas\\r2.txt".format(getcwd()))
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
            renglon=renglones[0]
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
        input("                    HA OCURRIDO UN ERROR DE PROCEDIMIENTO")
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
            visual.banner_turno="   {}            Crisbet - K ♦ - BurgerTown            {}   ".format(self.nombre_de_turno,self.nombre_cajero)
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


def cesar_fuente_grabado():
    while True:
        visual.cls()
        print("")
        texto=""
        print(texto)
        print("")
        clave=int(input("Clave: "))
        print("")
        print("                        Confirmar?")
        print("                    1.Si")
        print("                    2.No")
        selection=visual.prompt()
        if selection=="1":
            break
        elif selection=="2":
            texto="None"
            clave=0
        else:
            pass
    return [texto,clave]
def cesar_fuente_archivo():
    while True:
        visual.cls()
        print("")
        texto=escritor.leer_archivo_plano("{}/herramientas/cesar/leer.txt".format(getcwd()))
        print(texto)
        print("")
        clave=int(input("Clave: "))
        print("")
        print("                        Confirmar?")
        print("                    1.Si")
        print("                    2.No")
        selection=visual.prompt()
        if selection=="1":
            break
        elif selection=="2":
            texto="None"
            clave=0
        else:
            pass
    return [texto,clave]
def cesar_fuente_input():
    while True:
        visual.cls()
        print("")
        texto=input("Texto: ")
        print("")
        clave=int(input("Clave: "))
        print("")
        print("                        Confirmar?")
        print("                    1.Si")
        print("                    2.No")
        selection=visual.prompt()
        if selection=="1":
            break
        elif selection=="2":
            texto="None"
            clave=0
        else:
            pass
    return [texto,clave]
def cesar_fuente():
    while True:
        textoyclave=["None",0]
        visual.cls()
        print("")
        print("                       ELIJA LA FUENTE")
        print("                    1. Input")
        print("                    2. Archivo de texto")
        print("                    3. Grabado")
        selection=visual.prompt()
        if selection=="1":
            textoyclave=cesar_fuente_input()
            break
        elif selection=="2":
            textoyclave=cesar_fuente_archivo()
            break
        elif selection=="3":
            textoyclave=cesar_fuente_grabado()
            break
        else:
            pass
    return textoyclave
def cesar_encriptar():
    textoyclave=cesar_fuente()
    while True:
        texto=textoyclave[0]
        clave=textoyclave[1]
        visual.cls()
        print("=====ENCRIPTADO=====")
        print(cesar.encriptar(texto,clave))
        print("====ENCRIPTADO y ASCII====")
        print(escritor.chr_ascii(cesar.encriptar(texto,clave)))
        print("                         Elija el resultado")
        print("                    1. Guardar en archivo.txt")
        print("                    2. Guardar en archivo.txt formato ascii")
        print("                    3. Volver a encriptar")
        print("                    4. Volver al menú")
        selection=visual.prompt()
        if selection=="1":
            escritor.crear_archivo_plano("{}/herramientas/cesar/encriptado.txt".format(getcwd()),cesar.encriptar(texto,clave))
            escritor.cambiar_r2("cesar_main()")
            break
        elif selection=="2":
            escritor.crear_archivo_plano("{}/herramientas/cesar/encriptado.txt".format(getcwd()),escritor.chr_ascii(cesar.encriptar(texto,clave)))
            escritor.cambiar_r2("cesar_main()")
            break
        elif selection=="3":
            escritor.cambiar_r2("cesar_encriptar()")
            break
        elif selection=="4":
            escritor.cambiar_r2("cesar_main()")
            break
        else:
            pass
    return 0
def cesar_desencriptar():
    textoyclave=cesar_fuente()
    while True:
        texto=textoyclave[0]
        clave=textoyclave[1]
        visual.cls()
        print("=====DESENCRIPTADO=====")
        print(cesar.desencriptar(texto,clave))
        print("====DESENCRIPTADO y ASCII====")
        try:
            print(cesar.desencriptar(escritor.ascii_chr(texto),clave))
        except:
            print("NO DISP.")
        print("")
        print("                         Elija el resultado")
        print("                    1. Guardar en archivo.txt")
        print("                    2. Guardar en archivo.txt formato ascii")
        print("                    3. Volver a encriptar")
        print("                    4. Volver al menú")
        selection=visual.prompt()
        if selection=="1":
            escritor.crear_archivo_plano("{}/herramientas/cesar/desencriptado.txt".format(getcwd()),cesar.desencriptar(texto,clave))
            escritor.cambiar_r2("cesar_main()")
            break
        elif selection=="2":
            escritor.crear_archivo_plano("{}/herramientas/cesar/desencriptado.txt".format(getcwd()),cesar.desencriptar(escritor.ascii_chr(texto),clave))
            escritor.cambiar_r2("cesar_main()")
            break
        elif selection=="3":
            escritor.cambiar_r2("cesar_desencriptar()")
            break
        elif selection=="4":
            escritor.cambiar_r2("cesar_main()")
            break
        else:
            pass
    return 0
def cesar_main():
    while True:
        visual.cls()
        print("")
        print("                          CESAR")
        print("                    1. Encriptar")
        print("                    2. Desencriptar")
        print("                    3. Volver")
        selection=visual.prompt()
        if selection=="1":
            escritor.cambiar_r2("cesar_encriptar()")
            break
        elif selection=="2":
            escritor.cambiar_r2("cesar_desencriptar()")
            break
        elif selection=="3":
            escritor.cambiar_r2("logout")
            break
        else:
            pass
    return 0



def main_loop():
    while True:
        visual.cls()
        print("")
        print("                       HERRAMIENTAS")
        print("                    1. Cesar")
        print("                    2. Escritor Lector")
        print("                    3. Impresora")
        print("                    4. Salir")
        selection=visual.prompt()
        if selection=="1":
            r1=cesar_main()
            while True:
                r1=escritor.obtener_r2()
                if r1=="logout":
                    break
                else:
                    exec("{}".format(r1))
        elif selection=="4":
            visual.cls()
            break
        else:
            pass

main_loop()