import os
import subprocess
import getpass
from os import getcwd,listdir
from datetime import datetime
from traceback import format_exc
from tabulate import tabulate


"""
CLASES PRIMARIAS (SE DEBEN DECLARAR OBJETOS DE CADA CUAL)
"""
class Data:
    def __init__(self):
        self.ruta_temporales="{}\\data\\temp".format(getcwd())
        self.ruta_locales="{}\\data\\local".format(getcwd())
        self.rutas={
            "r2":"{}\\r2".format(self.ruta_temporales),
            "productos":"{}\\productos".format(self.ruta_locales),
            "id":"{}\\ventas\\id.txt".format(self.ruta_locales),
            "oculta":"{}\\cesar\\elvago".format(self.ruta_locales)}
        #Crear consultor de db
        self.consultor=Consultor()
        self.consultor.iniciar_codificador(self.obtener_secuencia())
        #-
        self.productos=self.obtener_productos()
    def cambiar_vbs(self,nombre):
        with self.consultor.leer_archivo_fijo("{}\\vbs\\{}.txt".format(self.ruta_locales,nombre)) as vbs:
            self.crear_archivo_plano("{}\\auxil.vbs".format(self.ruta_temporales),vbs)
    def obtener_secuencia(self):
        secuencia=self.consultor.leer_archivo_plano("{}\\secuencia.txt".format(self.rutas["oculta"])).split("\n")
        abc=str()
        for caracter in secuencia:
            abc=abc+chr(int(caracter))
        return abc
    def obtener_productos(self):
        productos=list()
        for codigo in listdir(self.rutas["productos"]):
            info={}
            for detalle in listdir("{}\\{}".format(self.rutas["productos"],codigo)):
                info["{}".format(detalle[:-4])]=self.consultor.leer_archivo_fijo("{}\\{}\\{}".format(self.rutas["productos"],codigo,detalle))
            productos.append(info)
        return productos
    def obtener_producto(self,codigo):
        producto={}
        for detalle in listdir("{}\\{}".format(self.rutas["productos"],codigo)):
            producto["{}".format(detalle[:-4])]=self.consultor.leer_archivo_fijo("{}\\{}\\{}".format(self.rutas["productos"],codigo,detalle))
        return producto
class Buscador:
    def __init__(self):
        self.data=Data_Buscador()
    def buscar(self,datos,busqueda):
        resultados=[]
        for elemento in datos:
            if busqueda.lower() in elemento["nombre"].lower():
                resultados.append(elemento)
        return resultados

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
class Cajero:
    def __init__(self):
        self.data=Data_Cajero()
        info=self.data.iniciar()
        self.nombre_cajero=info[0]
        self.nivel_privilegio=info[1]
class Cesar:
    def __init__(self):
        self.data=Data_Cesar()
class UI:
    def __init__(self):
        self.visual=Visual()
        self.visual_pedido=Visual_Pedido()
        self.data=Data_UI()
        pedido.data.detalles["Tipo de Precio"]=self.establecer_tipoprecio()
    def establecer_tipoprecio(self):
        tipo_de_precio=str()
        while True:
            self.visual.cls()
            print(self.visual.separador)
            print(" K♦ | INICIANDO PEDIDO:.. {}".format(pedido.data.detalles["ID"]))
            print(self.visual.separador)
            self.visual.menu("ELIJA EL TIPO DE PRECIO",["Precio Local","Precio Pedidos Ya"])
            selection=self.visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                break
            if selection=="1":
                tipo_de_precio = "local"
                break
            elif selection=="2":
                tipo_de_precio = "p.ya"
                break
            else:
                pass
        return tipo_de_precio
    def main_loop(self):
        while True:
            self.visual.cls()
            self.visual_pedido.banner_pedido()
            self.visual_pedido.vista_previa_pedido_mainloop()
            self.visual.menu("MENU DE OPCIONES",["Modificar Productos","Modificar Info","Vista Previa","Marchar Pedido"])
            selection=self.visual.prompt(cajero.nombre_cajero)
            if selection=="0":
                break
            elif selection=="1":
                r1=self.modificar_productos()
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
                r1=self.modificar_info()
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
            elif selection=="3":
                r1=self.vista_previa()
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
            elif selection=="4":
                r1=self.marchar_pedido()
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
            else:
                pass
    def modificar_productos(self):
        while True:
            self.visual.cls()
            self.visual_pedido.banner_pedido()
            self.visual_pedido.vista_previa_tabla_productos()
            self.visual.menu("MODIFICAR PRODUCTOS",["Agregar Productos","Eliminar Productos"])
            selection=self.visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                self.data.cambiar_r2("self.agregar_productos()")
                break
            elif selection=="2":
                self.data.cambiar_r2("self.eliminar_productos()")
                break
            elif selection=="0":
                self.data.cambiar_r2("logout")
                return "logout"
            else:
                pass
        return 0
    def agregar_productos(self):
        buscador=Buscador()
        while True:
            self.visual.cls()
            self.visual_pedido.banner_pedido()
            self.visual.titulo("AGREGAR PRODUCTOS")
            busqueda=self.visual.prompt("Buscar")
            resultados=buscador.buscar(buscador.data.obtener_carta(),busqueda)

            nombres=[]
            for r in resultados:
                nombres.append(r["nombre"])
            
            self.visual.menu("{} RESULTADOS".format(len(resultados)),nombres)
            selection=self.visual.prompt(cajero.nombre_cajero)
            if selection=="0":
                self.data.cambiar_r2("self.modificar_productos()")
                break
            elif int(selection)<=len(resultados):
                self.data.cambiar_r2("self.iniciar_producto({})".format(resultados[int(selection)-1]))
                break
            else:
                pass
        return 0
    def iniciar_producto(self,prod):
        producto=Producto(prod)
        interfaz_producto=UI_Producto(producto)

class Pedido:
    def __init__(self):
        self.data=Data_Pedido()
        self.visual=Visual_Pedido()
    def agregar_producto(self,producto):
        self.data.productos.append(producto)
        precio=producto["Total"]
        precio=int(precio[0])
        self.data.finanzas["Subtotal"]=self.data.finanzas["Subtotal"]+precio
class UI_Producto(UI):
    def __init__(self,prod):
        super.init()
        self.producto=prod
        self.visual_producto=Visual_Producto()
    def cambiar_cantidad(self):
        while True:
            self.visual.cls()
            self.visual_pedido.banner_pedido()
            self.visual.titulo(produ)
class Producto:
    def __init__(self,info):
        self.info=info
        self.detalles={#ESTO RETORNAMOS; A LA HORA DE RETORNAR AGREGAMOS EL TOTAL
            "Cantidad":[]
            "Nombre":[]
            "Subtotal":[]}
        self.detalles["Cantidad"].append(interfaz_producto.cambiar_cantidad())
    def retornar_total(self):
        cantidad_total=0
        subtotal_total=0
        for cantidad in self.detalles["Cantidad"]:
            if cantidad == "":
                pass
            else:
                cantidad_total=cantidad_total+int(cantidad)
        for subtotal in self.detalles["Subtotal"]:
            if subtotal=="":
                pass
            else:
                subtotal_total=subtotal_total+int(subtotal)
        return cantidad_total*subtotal_total
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
    def banner(self,banner):
        print("")
        print(self.separador)
        print(self.espaciado(banner,80))
        print(self.separador)
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
        self.clave_turno=int()
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
            txt.write(self.codificador.chr_ascii(self.codificador.encriptar(str(texto),cesar.data.clave_turno)))
            txt.close()
    def leer_archivo_turno(self,ruta):
        with open(ruta,"r") as txt:
            texto=txt.read()
            txt.close()
        return self.codificador.desencriptar(self.codificador.ascii_chr(texto),cesar.data.clave_turno)
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
class Visual_Producto(Visual):
    def __init__(self):
        super.__init__()

class Visual_Pedido(Visual):
    def __init__(self):
        super().__init__()
    def banner_pedido(self):
        info=[]
        info.append(pedido.data.detalles["ID"])
        info.append(pedido.data.detalles["Cajero"])
        info.append(str(len(pedido.data.productos)))
        info.append(pedido.data.detalles["Tipo de Precio"])
        info.append(pedido.data.detalles["Fecha"])
        print("")
        print(self.separador)
        print(" K♦ |   ID:{} - {} - {} Producto(s) - Precio {} - {}".format(*info))
        print(self.separador)
    def vista_previa_descuento(self,descuento,subtotal):
        porcentaje=descuento/subtotal
        porcentaje=porcentaje*100
        info={
            "SUBTOTAL" : [subtotal],
            "DESC. PORCENTAJE" : ["%{}".format(porcentaje)],
            "DESC. MONTO" : [descuento],
            "TOTAL" : [subtotal-descuento]}
        banner=tabulate(info,headers="keys",tablefmt="fancy_grid",stralign="center")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_recargo(self,recargo,subtotal):
        porcentaje=recargo/subtotal
        porcentaje=porcentaje*100
        info={
            "SUBTOTAL" : [subtotal],
            "RECR. PORCENTAJE" : ["%{}".format(porcentaje)],
            "RECR. MONTO" : [recargo],
            "TOTAL" : [subtotal+recargo]}
        banner=tabulate(info,headers="keys",tablefmt="fancy_grid",stralign="center")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_tabla_productos(self):
        
        banner=tabulate(info,headers="keys",tablefmt="fancy_grid",stralign="left")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_pedido_mainloop(self):
        info={
            "ID":[pedido.data.detalles["ID"]],
            "MET.PAGO":[pedido.data.detalles["Metodo de pago"]],
            "MET. ENTREGA":[pedido.data.detalles["Metodo de entrega"]],
            "PRODUCTOS":["{} Productos".format(len(pedido.data.productos))],
            "SUBTOTAL":[str(pedido.data.finanzas["Subtotal"])]}
        banner=tabulate(info, headers="keys",tablefmt="fancy_grid",stralign="center")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_producto(self):
        info={
            "CANT.":[str(producto.cantidad)],
            "NOMBRE":[producto.nombre+producto.comentarios],
            "P. INDIV.":[str(producto.precio_individual)],
            "P. TOTAL":[str(int(producto.precio_individual)*int(producto.cantidad))]}
        banner=tabulate(info, headers="keys",tablefmt="fancy_grid",stralign="left")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_pedido(self):
        #DETALLES DEL PEDIDO
        try:
            r_porc=str((pedido.recargo_monto/pedido.subtotal)*100)
            d_porc=str((pedido.descuento_monto/pedido.subtotal)*100)
            total=str(pedido.subtotal+pedido.recargo_monto-pedido.descuento_monto)
        except:
            r_porc="0.0"
            d_porc="0.0"
            total="0"
        hora=operative_sist.obtener_hora()
        print("")
        print(self.espaciado(pedido.metodo_de_entrega,80))
        info_detalles={
            1:["ID {}".format(pedido.id),pedido.fecha,pedido.metodo_de_pago,"Subtotal","Descuento %{}".format(d_porc),"Recargo %{}".format(r_porc),"Total"],
            2:["{} Productos".format(len(pedido.productos)),hora,pedido.cajero,"$ {}".format(str(pedido.subtotal)),"$ {}".format(str(pedido.descuento_monto)),"$ {}".format(str(pedido.recargo_monto)),"$ {}".format(total)]}
        tabla_detalles=tabulate(info_detalles,tablefmt="fancy_grid",stralign="left")
        renglones=tabla_detalles.split("\n")
        espacios=80-len(renglones[0])
        for renglon in renglones[:6]:
            x=0
            while x<=espacios/2:
                print(" ",end="")
                x=x+1
            print(renglon)
        #PRODUCTOS DEL PEDIDO
        cantidades=list()
        nombres=list()
        individuales=list()
        totales=list()
        for prod in pedido.productos:
            prod=prod.split(",")
            cantidades.append(prod[0])
            nombres.append(prod[1])
            individuales.append(prod[2])
            totales.append(prod[3])
        info_productos={
            "CANT.":cantidades,
            "NOMBRE    ":nombres,
            "P.UNI.":individuales,
            "P.TOTAL":totales}
        tabla_productos=tabulate(info_productos,tablefmt="fancy_grid",headers="keys",stralign="left")
        print(self.espaciado(tabla_productos,80))
        #PRECIOS DEL PEDIDO
        for renglon in renglones[7:]:
            x=0
            while x<=espacios/2:
                print(" ",end="")
                x=x+1
            print(renglon)
    def modificando_hamburgesa(self,nombre="NULL",modificaciones="#"):
        info={
            "Nombre":[nombre],
            "Modificaciones":[modificaciones]
        }
        banner=tabulate(info, headers="keys",tablefmt="fancy_grid",stralign="center")
        print(self.espaciado(banner,80))
        print(self.separador)
class Data_Pedido(Data):
    def __init__(self):
        super().__init__()
        self.detalles={
            "Metodo de entrega":"null",
            "Metodo de pago":"null",
            "ID":str(self.obtener_id()),
            "Cajero":"Cajero {}".format(cajero.nombre_cajero.capitalize()),
            "Fecha":tiempo.obtener_fecha_numeros(),
            "Hora de confirmacion":"null",
            "Tipo de Precio":"null"}
        self.productos=list()
        self.finanzas={
            "Subtotal":0,
            "Descuento Monto":0.0,
            "Recargo Monto":0.0,
            "Total":0.0}
    def obtener_id(self):
        i=int(self.consultor.leer_archivo_fijo(self.rutas["id"]))+1
        self.consultor.crear_archivo_fijo(self.rutas["id"],str(i))
        return self.consultor.leer_archivo_fijo(self.rutas["id"])
class Data_Cajero(Data):
    def __init__(self):
        super().__init__()
    def iniciar(self):
        dir=listdir("{}\\turno".format(self.ruta_temporales))
        self.nombre_de_turno=dir[0]
        self.ruta_turno="{}\\turno\\{}".format(self.ruta_temporales,self.nombre_de_turno)
        self.rutas_turno={
            "info":"{}\\info".format(self.ruta_turno),
            "retirados":"{}\\retirados".format(self.ruta_turno),
            "armando":"{}\\armando".format(self.ruta_turno),
            "marchando":"{}\\marchando".format(self.ruta_turno)}
        self.clave_turno=int(self.consultor.leer_archivo_fijo("{}\\key.txt".format(self.rutas_turno["info"])))
        return self.consultor.leer_archivo_fijo("{}\\cajero.txt".format(self.rutas_turno["info"])).split(",")
class Data_UI(Data):
    def __init__(self):
        super().__init__()
    def cambiar_r2(self,texto):
        self.consultor.crear_archivo_turno("{}\\pedido.txt".format(self.rutas["r2"]),texto)
    def obtener_r2(self):
        return self.consultor.leer_archivo_turno("{}\\pedido.txt".format(self.rutas["r2"]))
class Data_Cesar(Data):
    def __init__(self):
        super().__init__()
        self.accounts=self.consultor.leer_archivo_fijo("{}\\accounts.txt".format(self.rutas["oculta"])).split("\n")
        self.secuencia=super().obtener_secuencia()
        self.clave_turno=cajero.data.clave_turno
class Data_Buscador(Data):
    def __init__(self):
        super().__init__()
        self.tpdp=pedido.data.detalles["Tipo de Precio"]
    def obtener_carta(self):
        productos=super().obtener_productos()
        carta=[]
        for producto in productos:
            if self.tpdp=="local":
                codigo=producto["codigo"]
                c=codigo.split("-")
                if c[0]=="0":
                    if c[1]=="2":
                        if c[2]=="1":
                            pass
                        else:
                            carta.append(producto)
                    else:
                        carta.append(producto)

            elif self.tpdp=="p.ya":
                codigo=producto["codigo"]
                c=codigo.split("-")
                if c[0]=="1":
                    if c[1]=="2":
                        if c[2]=="1":
                            pass
                        else:
                            carta.append(producto)
                    else:
                        carta.append(producto)
                
        return carta
    def obtener_topings(self):
        productos=super().obtener_productos()
        topings=[]
        for producto in productos:
            codigo=producto["codigo"]
            c=codigo.split("-")
            if c[1]=="2":
                if c[2]=="1":
                    topings.append(producto)
                else:
                    pass
            else:
                pass
        return topings
    def obtener_elementos(self):
        pass
class Data_Producto(Data):
    def __init__(self,info):




"""
DECLARACIONES
"""
sistema=Sistema()
tiempo=Tiempo()
data=Data()
cajero=Cajero()
pedido=Pedido()
cesar=Cesar()
interfaz=UI()

interfaz.main_loop()
