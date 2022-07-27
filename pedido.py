import os
import subprocess
from os import getcwd,listdir
from datetime import datetime
from traceback import format_exc
from tabulate import tabulate

# Crisbet beta 

###CLASES DEL BACKEND
class OS():
    def __init__(self):
        self.ruta_temporales="{}\\data\\temp".format(getcwd())
        self.ruta_locales="{}\\data\\local".format(getcwd())
        self.ruta_productos="{}\\productos".format(self.ruta_locales)
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
        return str(fecha)
    def obtener_fecha_letras(self):
        fecha=datetime.today().strftime("%A, %B %d, %Y")
        return fecha
    def obtener_hora(self):
        now=datetime.now()
        hora=now.strftime("%H:%M:%S")
        return str(hora)
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
        self.ruta_id="{}\\ventas\\id.txt".format(operative_sist.ruta_locales)
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
    def cambiar_vbs(self,nombre):
        ###AHREEEEEEE?
        self.crear_archivo_plano("{}\\auxil.vbs".format(operative_sist.ruta_temporales),self.leer_archivo_fijo("{}\\vbs\\{}.txt".format(operative_sist.ruta_locales,nombre)))
    def obtener_id_pedido(self):
        i=int(self.leer_archivo_fijo(self.ruta_id))+1
        self.crear_archivo_fijo(self.ruta_id,str(i))
        return self.leer_archivo_fijo(self.ruta_id)
    def elegir_producto(self,codigo):        
        ruta="{}\\{}".format(operative_sist.ruta_productos,codigo)
        producto=list()
        #############################################
        producto.append(self.leer_archivo_fijo("{}\\nombre.txt".format(ruta)))
        producto.append(self.leer_archivo_fijo("{}\\precio.txt".format(ruta)))
        producto.append(self.leer_archivo_fijo("{}\\stock.txt".format(ruta)))
        producto.append(self.leer_archivo_fijo("{}\\selection.txt".format(ruta)))
        try:
            producto.append(self.leer_archivo_fijo("{}\\elementos.txt".format(ruta)))
        except:
            producto.append("null")
        if codigo[2]=="0":
            producto.append(self.leer_archivo_fijo("{}\\ingredientes.txt".format(ruta)))
        else:
            pass
        producto.append(codigo)
        return producto
    def obtener_database_buscador(self,tipo_de_precio):
        nombres=list()
        codigos=list()
        if tipo_de_precio=="p.ya":
            nombres=self.leer_archivo_plano("{}\\nombres_pya.txt".format(operative_sist.ruta_productos)).split("\n")
            codigos=self.leer_archivo_plano("{}\\codigos_pya.txt".format(operative_sist.ruta_productos)).split("\n")
        elif tipo_de_precio=="local":
            nombres=self.leer_archivo_plano("{}\\nombres_local.txt".format(operative_sist.ruta_productos)).split("\n")
            codigos=self.leer_archivo_plano("{}\\codigos_local.txt".format(operative_sist.ruta_productos)).split("\n")
        return[nombres,codigos]
    def obtener_nombre_prod(self,codigos):
        nombres=list()
        for codigo in codigos:
            nombres.append(self.leer_archivo_fijo("{}\\{}\\nombre.txt".format(operative_sist.ruta_productos,codigo)))
        return nombres
class Cesar():
    def __init__(self):
        self.ruta_locales="{}\\data\\local\\cesar".format(getcwd())
        self.ruta_temporales="{}\\data\\temp\\cesar".format(getcwd())
        self.ruta_oculta="{}\\elvago".format(self.ruta_locales)
        self.secuencia=self.obtener_secuencia_DB()
        self.clave_fija=self.obtener_clave_fija_DB()
        self.clave_turno=int()
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
###DECLARACIÓN DE AGENTES DEL BACKEND(el orden es importante)
operative_sist=OS()
escritor=Escritor_Lector()
cesar=Cesar()

###CLASES DEL FRONTEND
class Promo():
    def __init__(self):
        self.nombre=str()
        self.precio_individual=0
        self.descuento=int()
        self.stock=str()
        self.codigo=str()
        self.productos=list()
        self.comentarios=str()
        self.cantidad=int()
    def iniciar(self,info):
        self.nombre=info[0]
        self.descuento=info[1]
        self.stock=info[2]
        if self.stock.lower()=="si":
            pass
        else:
            while True:
                visual.cls()
                visual.banner_pedido()
                visual.menu("{} FUERA DE STOCK".format(self.nombre),["Agregar de Todas Formas"])
                selection=visual.prompt(cajero.nombre_cajero.capitalize())
                if selection=="1":
                    break
                elif selection=="0":
                    escritor.cambiar_r2("pedido.agregar_productos()")
                    return 0
                else:
                    pass
        self.elementos=info[3].split("\n")
        self.productos=info[4].split("\n")
        self.codigo=info[-1]
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("AGREGANDO",self.nombre)
            try:
                self.cantidad=int(visual.prompt("Cantidad"))
                break
            except:
                visual.cls()
                print("")
                print("                     LA CANTIDAD DEBE SER UN NÚMERO ENTERO")
                input("                    ========================================                    ")
        escritor.cambiar_r2("promo.main_loop()")
        return 0
    def main_loop(self):
        e=0
        for producto in productos:
            p=producto.split(":")
            cantidad_maxima=int(p[0])*int(self.cantidad)
            producto=p[1]
            codigos=p[2].split(",")
            nombres=escritor.obtener_nombre_prod(codigos)
            c=0
            while c<<cantidad_maxima:
                while True:
                    visual.cls()
                    visual.banner_pedido()
                    visual.titulo("AGREGAR {}".format(producto.upper()),"Buscador de Productos")
                    info=buscador(nombres,codigos)
                    if info==0:
                        pass
                    else:
                        while True:
                            visual.cls()
                            visual.banner_pedido()
                            visual.titulo("AGREGANDO {}".format(info[1]),"Cantidad Máx: {}".format(cantidad_maxima-c))
                            try:
                                cantidad=int(visual.prompt("Cantidad"))
                                break
                            except:
                                visual.cls()
                                print("")
                                print("                     LA CANTIDAD DEBE SER UN NÚMERO ENTERO")
                                input("                    ========================================                    ")
                        if cantidad<=cantidad_maxima:
                            antes=len(pedidos.productos)
                            producto.iniciar(info,int(cantidad))
                            despues=len(pedido.productos)
                            if antes==despues:
                                pass
                            else:
                                c=c+cantidad
                            break
                        else:
                            pass
        return 0

            

class Producto():
    def __init__(self):
        self.nombre=str()
        self.precio_individual=int()
        self.stock=str()
        self.selection=str()
        self.elementos=str()
        self.codigo=str()
        self.ingredientes=str()
        self.comentarios=str()
        self.cantidad=int()
    def iniciar(self,producto,cantidad="null"):
        self.nombre=producto[0]
        self.precio_individual=producto[1]
        self.stock=producto[2]
        self.selection=producto[3]
        self.elementos=producto[4]
        self.codigo=producto[-1]
        ############################
        if self.codigo[2]=="0":
            self.ingredientes=producto[5]
        else:
            pass
        if self.stock.lower()=="si":
            pass
        else:
            while True:
                visual.cls()
                visual.banner_pedido()
                visual.menu("{} FUERA DE STOCK".format(self.nombre),["Agregar de Todas Formas"])
                selection=visual.prompt(cajero.nombre_cajero.capitalize())
                if selection=="1":
                    break
                elif selection=="0":
                    escritor.cambiar_r2("pedido.agregar_productos()")
                    return 0
                else:
                    pass
        if cantidad=="null":
            while True:
                visual.cls()
                visual.banner_pedido()
                visual.titulo("AGREGANDO",self.nombre)
                try:
                    self.cantidad=int(visual.prompt("Cantidad"))
                    break
                except:
                    visual.cls()
                    print("")
                    print("                     LA CANTIDAD DEBE SER UN NÚMERO ENTERO")
                    input("                    ========================================                    ")
        else:
            self.cantidad=int(cantidad)
        escritor.cambiar_r2("producto.main_loop()")
        return 0
    def main_loop(self):
        if self.selection=="hamburgesa":
            opciones=["Confirmar Producto","Opciones Avanzadas","Quitar Topings","Agregar Topings"]
        else:
            opciones=["Confirmar Producto","Opciones Avanzadas"]
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.vista_previa_producto()
            visual.menu("{}S -- MENU PRINCIPAL".format(self.selection.upper()),opciones)
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                escritor.cambiar_r2("pedido.mod_productos()")
                break
            elif selection=="1":
                pedido.confirmar_producto("{},{},{},{}".format(self.cantidad,self.nombre,self.precio_individual,str(int(self.precio_individual)*int(self.cantidad))))
                escritor.cambiar_r2("logout")
                break
            elif selection=="2":
                escritor.cambiar_r2("producto.opciones_avanzadas()")
                break
            elif selection=="3":
                if self.selection=="hamburgesa":
                    escritor.cambiar_r2("producto.quitar_topings()")
                    break
            elif selection=="4":
                if self.selection=="hamburgesa":
                    escritor.cambiar_r2("producto.agregar_topings()")
                    break
            else:
                pass
        return 0
    def opciones_avanzadas(self):
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.vista_previa_producto()
            visual.menu("{}S - OPCIONES AVANZADAS".format(self.selection.upper()),["Agregar Comentario","Eliminar Comentario","Agregar Descuento","Agregar Recargo","Cambiar Cantidad"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                escritor.cambiar_r2("producto.main_loop()".format(self.selection))
                break
            elif selection=="1":
                self.agregar_comentario()
            elif selection=="2":
                self.eliminar_comentario()
            elif selection=="3":
                self.precio_individual=str(int(self.precio_individual)-int(cajero.agregar_descuento(self.precio_individual)))
                break
            elif selection=="4":
                self.precio_individual=str(int(self.precio_individual)+int(cajero.agregar_recargo(self.precio_individual)))
                break
            elif selection=="5":
                escritor.cambiar_r2("producto.cambiar_cantidad()")
                break
            else:
                pass
        return 0
    def eliminar_comentario(self):
        comentarios=self.nombre.split("\n")
        comentarios=comentarios[1:]
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.menu("{}S - ELIMINAR COMENTARIO".format(self.selection.upper()),comentarios)
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                break
            elif int(selection)<=len(comentarios):
                try:
                    a=self.nombre.split("\n")
                    b=a[0]
                    a=a[1:]
                    a.pop(int(selection)-1)
                    for c in a:
                        b=b+"\n"+c
                    self.nombre=b
                    break
                except:
                    pass
            else:
                pass
    def agregar_comentario(self):
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("{}S".format(self.selection.upper()),"Agregar Comentario")
            comentario=visual.prompt("Comentario")
            visual.cls()
            visual.banner_pedido()
            visual.titulo("{}S - AGREGAR COMENTARIO".format(self.selection.upper()),"# {}".format(comentario))
            visual.confirmar()
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                self.nombre=self.nombre+"\n#"+comentario.upper()
                break
            elif selection=="2":
                break
            else:
                pass
    def cambiar_cantidad(self):
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("CAMBIAR CANTIDAD",self.nombre)
            try:
                cantidad=int(visual.prompt("Cantidad"))
                visual.confirmar()
                selection=visual.prompt(cajero.nombre_cajero.capitalize())
                if selection=="1":
                    self.cantidad=str(cantidad)
                    break
                elif selection=="2":
                    break
                else:
                    pass
            except:
                pass
        escritor.cambiar_r2("producto.main_loop()".format(self.selection))
        return 0
    def agregar_topings(self):
        no,co=escritor.obtener_database_buscador(pedido.tipo_de_precio)
        nombres=list()
        codigos=list()
        x=0
        for codigo in co:
            c=codigo.split("-")
            if c[1]=="2":
                if c[2]=="1":
                    codigos.append(codigo)
                    nombres.append(no[x])
                else:
                    pass
            else:
                pass
            x=x+1
        agregar=list()
        while True:
            a_str=str().join(agregar)
            visual.cls()
            visual.banner_pedido()
            visual.modificando_hamburgesa(self.nombre,a_str)
            print(visual.espaciado(tabulate({1:["BUSCADOR DE TOPINGS"]},tablefmt="fancy_grid",stralign="center"),80))
            resultados=buscador(nombres,codigos,"corto")
            print("                    ________________________________________                    ")
            print(visual.espaciado("{} Resultados".format(len(resultados)),80))
            print("                    ________________________________________")
            x=1
            for resultado in resultados:
                print("                       {}    |   {}".format(x,resultado))
                print("                    ----------------------------------------")
                x=x+1
            print("                   |   0    |   Confirmar                   |")
            print("                    ----------------------------------------")
            print("                   |   00   |   Equivocacion                |")
            print("                    ----------------------------------------")
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                for a in agregar:
                    self.nombre=self.nombre+"\n"+a
                escritor.cambiar_r2("producto.main_loop()")
                break
            elif selection=="00":
                try:
                    agregar.pop()
                except:
                    pass
            elif int(selection)<=x:
                try:
                    agregar.append("c/ {} ".format(resultados[int(selection)-1]))
                except:
                    pass
            else:
                pass
        return 0
    def quitar_topings(self):
        topings=self.ingredientes.split(",")
        topings=topings[2:]
        quitar=list()
        while True:
            q_str=str().join(quitar)
            visual.cls()
            visual.banner_pedido()
            visual.modificando_hamburgesa(self.nombre,q_str)
            print("                    ________________________________________                    ")
            print(visual.espaciado("HAMBURGUESAS - QUITAR TOPINGS",80))
            print("                    ________________________________________")
            print("                    ----------------------------------------")
            x=1
            for toping in topings:
                print("                       {}    |   {}".format(x,toping))
                print("                    ----------------------------------------")
                x=x+1
            print("                   |   0    |   Continuar                   |")
            print("                    ----------------------------------------")
            print("                   |   00   |   Equivocacion                |")
            print("                    ----------------------------------------")
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                for q in quitar:
                    self.nombre=self.nombre+"\n"+q
                escritor.cambiar_r2("producto.main_loop()")
                break
            elif selection=="00":
                try:
                    quitar.pop()
                except:
                    pass
            elif int(selection)<=len(topings):
                try:
                    toping=topings[int(selection)-1]
                    quitar.append("s/ {} ".format(toping))
                except:
                    pass
            else:
                pass
        return 0

class Visual():
    def __init__(self):
        self.ruta="{}\\visual".format(operative_sist.ruta_locales)
        self.ruta_banners="{}\\banners".format(self.ruta)
        ####################################################
        self.banner_turno=str()
        self.separador="________________________________________________________________________________"
    def cls(self):
        os.system("cls")
    def prompt(self,nombre="UserUnknown"):
        print("                    ________________________________________                    ")
        print(self.espaciado(nombre.capitalize(),80))
        print("                    ________________________________________                    ")
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
    def banner_pedido(self):
        print("")
        print(self.separador)
        print(" K♦ |   ID:{} - {} - {} Producto(s) - Precio {} - {}".format(pedido.id,pedido.cajero,len(pedido.productos),pedido.tipo_de_precio.capitalize(),pedido.fecha))
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
        info={
            "CANT.":cantidades,
            "NOMBRE":nombres,
            "P. INDIV.":individuales,
            "P. TOTAL":totales}
        banner=tabulate(info,headers="keys",tablefmt="fancy_grid",stralign="left")
        print(self.espaciado(banner,80))
        print("")
        print(self.separador)
    def vista_previa_pedido_mainloop(self):
        info={
            "ID":[pedido.id],
            "MET.PAGO":[pedido.metodo_de_pago],
            "MET. ENTREGA":[pedido.metodo_de_entrega],
            "PRODUCTOS":["{} Productos".format(len(pedido.productos))],
            "SUBTOTAL":[pedido.subtotal]}
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
    def menu(self,titulo,opciones):
        print("")
        print("                    ________________________________________                    ")
        print(self.espaciado(titulo,80))
        print("                    ________________________________________")
        print("")
        print("                    ----------------------------------------")
        x=1
        for opcion in opciones:
            print("                       {}    |   {}".format(x,opcion))
            print("                    ----------------------------------------")
            x=x+1
        print("                   |   0    |   Volver     ♦     Cancelar   |")
        print("                    ----------------------------------------")
    def titulo(self,titulo,subtitulo=""):
        info={1:[titulo,subtitulo]}
        print(self.espaciado(tabulate(info,tablefmt="fancy_grid",stralign="center"),80))
    def confirmar(self):
        print("                    ________________________________________                    ")
        print(self.espaciado("CONFIRMAR?",80))
        print("                    ________________________________________")
        print("                    ----------------------------------------")
        print("                   |   1    |   Si                          |")
        print("                    ----------------------------------------")
        print("                   |   2    |   No (Volver ♦ Cancelar)      |")
        print("                    ----------------------------------------")
    def modificando_hamburgesa(self,nombre="NULL",modificaciones="#"):
        info={
            "Nombre":[nombre],
            "Modificaciones":[modificaciones]
        }
        banner=tabulate(info, headers="keys",tablefmt="fancy_grid",stralign="center")
        print(self.espaciado(banner,80))
        print(self.separador)

class Cajero():
    def __init__(self):
        d=listdir("{}\\turno".format(operative_sist.ruta_temporales))
        self.nombre_de_turno=d[0]
        self.ruta_turno="{}\\turno\\{}".format(operative_sist.ruta_temporales,self.nombre_de_turno)
        self.ruta_turno_info="{}\\info".format(self.ruta_turno)
        self.ruta_retirados="{}\\retirados".format(self.ruta_turno)
        self.ruta_armando="{}\\armando".format(self.ruta_turno)
        self.ruta_marchando="{}\\marchando".format(self.ruta_turno)
        cesar.clave_turno=int(escritor.leer_archivo_fijo("{}\\key.txt".format(self.ruta_turno_info)))
        info=escritor.leer_archivo_turno("{}\\cajero.txt".format(self.ruta_turno_info)).split(",")
        self.nivel_privilegio=info[1]
        self.nombre_cajero=info[0]
    def agregar_descuento(self,subtotal):
        subtotal=int(subtotal)
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("AGREGAR DESCUENTO","Para agregar un porcentaje de descuento coloque '%' antes del mismo.\nPara agregar un monto de descuento coloque '$' antes del mismo.")
            print("")
            print("                    ----------------------------------------")
            print("                   |   0    |   Volver     ♦     Cancelar   |")
            print("                    ----------------------------------------")
            descuento=visual.prompt("Descuento")
            if descuento=="0":
                return 0
            elif descuento[0]=="%":
                try:
                    porcentaje=subtotal/100
                    porcentaje=porcentaje*int(descuento[1:])
                    while True:
                        visual.cls()
                        visual.banner_pedido()
                        visual.vista_previa_descuento(porcentaje,subtotal)
                        visual.confirmar()
                        selection=visual.prompt(cajero.nombre_cajero.capitalize())
                        if selection=="1":
                            return porcentaje
                        elif selection=="2":
                            return 0
                        else:
                            pass
                except:
                    pass
            elif descuento[0]=="$":
                try:
                    descuento=int(descuento[1:])
                    if descuento<=subtotal:
                        while True:
                            visual.cls()
                            visual.banner_pedido()
                            visual.vista_previa_descuento(descuento,subtotal)
                            visual.confirmar()
                            selection=visual.prompt(cajero.nombre_cajero.capitalize())
                            if selection=="1":
                                return descuento
                            elif selection=="2":
                                return 0
                            else:
                                pass
                    else:
                        pass
                except:
                    pass
            else:
                pass
    def agregar_recargo(self,subtotal):
        subtotal=int(subtotal)
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("AGREGAR RECARGO","Para agregar un porcentaje de recargo coloque '%' antes del mismo.\nPara agregar un monto de recargo coloque '$' antes del mismo.")
            print("")
            print("                    ----------------------------------------")
            print("                   |   0    |   Volver     ♦     Cancelar   |")
            print("                    ----------------------------------------")
            recargo=visual.prompt("Recargo")
            if recargo=="0":
                return 0
            elif recargo[0]=="%":
                try:
                    porcentaje=subtotal/100
                    porcentaje=porcentaje*int(recargo[1:])
                    while True:
                        visual.cls()
                        visual.banner_pedido()
                        visual.vista_previa_recargo(porcentaje,subtotal)
                        visual.confirmar()
                        selection=visual.prompt(cajero.nombre_cajero.capitalize())
                        if selection=="1":
                            return porcentaje
                        elif selection=="2":
                            return 0
                        else:
                            pass
                except:
                    pass
            elif recargo[0]=="$":
                try:
                    recargo=int(recargo[1:])
                    while True:
                        visual.cls()
                        visual.banner_pedido()
                        visual.vista_previa_recargo(recargo,subtotal)
                        visual.confirmar()
                        selection=visual.prompt(cajero.nombre_cajero.capitalize())
                        if selection=="1":
                            return recargo
                        elif selection=="2":
                            return 0
                        else:
                            pass
                except:
                    pass
            else:
                pass
        return 0
class Pedido():
    def __init__(self):
        #############################
        self.productos=list()
        ##########################
        self.metodo_de_entrega="null"
        self.metodo_de_pago="null"
        self.id=escritor.obtener_id_pedido()
        self.cajero="Cajero {}".format(cajero.nombre_cajero.capitalize())
        self.fecha=operative_sist.obtener_fecha_numeros()
        self.tipo_de_precio=str()
        self.hora_confirmacion=str()
        #############################
        self.subtotal=0
        self.descuento_monto=0.0
        self.recargo_monto=0.0
        self.total=0.0
    def mod_productos(self):
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.vista_previa_tabla_productos()
            visual.menu("MODIFICAR PRODUCTOS",["Agregar Productos","Eliminar Productos"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                escritor.cambiar_r2("pedido.agregar_productos()")
                break
            elif selection=="2":
                escritor.cambiar_r2("pedido.eliminar_productos()")
                break
            elif selection=="0":
                escritor.cambiar_r2("logout")
                return "logout"
            else:
                pass
        return 0
    def agregar_productos(self):
        no,co=escritor.obtener_database_buscador(self.tipo_de_precio)
        nombres=list()
        codigos=list()
        x=0
        for codigo in co:
            c=codigo.split("-")
            if c[1]=="2":
                if c[2]=="1":
                    pass
                else:
                    codigos.append(codigo)
                    nombres.append(no[x])
            else:
                codigos.append(codigo)
                nombres.append(no[x])
            x=x+1
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("AGREGAR PRODUCTOS","Buscador de Productos")
            info=buscador(nombres,codigos)
            if info==0:
                pass
            else:
                codigo_elegido=info[-1].split("-")
                if codigo_elegido[1]=="4":
                    escritor.cambiar_r2("promo.iniciar({})".format(info))
                else:
                    pass
                escritor.cambiar_r2("producto.iniciar({})".format(info))
                break
        return 0
    def confirmar_producto(self,producto):
        self.productos.append(producto)
        producto=producto.split(",")
        self.subtotal=self.subtotal+int(producto[-1])
    def mod_info(self):
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.menu("MODIFICAR INFORMACION",["Establecer Metodo de Entrega","Establecer Metodo de Pago","Agregar Descuento","Agregar Recargo"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                escritor.cambiar_r2("logout")
                return "logout"
            elif selection=="1":
                escritor.cambiar_r2("pedido.establecer_metododeentrega()")
                break
            elif selection=="2":
                escritor.cambiar_r2("pedido.establecer_metododepago()")
                break
            elif selection=="3":
                self.descuento_monto=self.descuento_monto+cajero.agregar_descuento(self.subtotal)
            elif selection=="4":
                self.recargo_monto=self.recargo_monto+cajero.agregar_recargo(self.subtotal)
            else:
                pass
        return 0
    def establecer_tipoprecio(self):
        tipo_de_precio=str()
        while True:
            visual.cls()
            print("")
            print("————————————————————————————————————————————————————————————————————————————————")
            print(" K♦ | INICIANDO PEDIDO:.. {}".format(self.id))
            print("————————————————————————————————————————————————————————————————————————————————")
            visual.menu("ELIJA EL TIPO DE PRECIO",["Precio Local","Precio Pedidos Ya"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
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
    def establecer_metododeentrega(self):
        metodo=str()
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.menu("METODO DE ENTREGA",["Enviar con Delivery","Retira en el Local","P.Ya Delivery","P.Ya Retira en el Local"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                escritor.cambiar_r2("pedido.mod_info()")
                return 0
            elif selection=="1":
                if self.tipo_de_precio=="local":
                    metodo="Enviar a"
                    break
            elif selection=="2":
                if self.tipo_de_precio=="local":
                    metodo="Retira"
                    break
            elif selection=="3":
                if self.tipo_de_precio=="p.ya":
                    metodo="P.ya"
                    break
            elif selection=="4":
                if self.tipo_de_precio=="p.ya":
                    metodo="P.ya ret. local"
                    break
            else:
                pass
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("METODO DE ENTREGA")
            cliente=input("                               {} ".format(metodo))
            visual.cls()
            visual.banner_pedido()
            visual.titulo("METODO DE ENTREGA","{} {}".format(metodo,cliente))
            visual.confirmar()
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                self.metodo_de_entrega="{} {}".format(metodo,cliente)
                escritor.cambiar_r2("pedido.mod_info()")
                return 0
            elif selection=="2":
                break
            else:
                pass
        return 0
    def establecer_metododepago(self):
        metodo=str()
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.menu("METODO DE PAGO",["Efectivo","Mercado Pago","P.Ya Efectivo","P.ya Pago Online"])
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                escritor.cambiar_r2("pedido.mod_info()")
                return 0
            elif selection=="1":
                if self.tipo_de_precio=="local":
                    metodo="Efectivo local"
                    break
            elif selection=="2":
                if self.tipo_de_precio=="local":
                    while True:
                        visual.cls()
                        visual.banner_pedido()
                        visual.titulo("METODO DE PAGO","Mercado Pago")
                        visual.menu("PAGAR CON",["Transferencia, Débito","Credito, QR, Link"])
                        selection=visual.prompt(cajero.nombre_cajero.capitalize())
                        if selection=="0":
                            escritor.cambiar_r2("pedido.establecer_metododepago()")
                            return 0
                        elif selection=="1":
                            metodo="Debito MP"
                            break
                        elif selection=="2":
                            metodo="Credito MP"
                            break
                        else:
                            pass
                    break
            elif selection=="3":
                if self.tipo_de_precio=="p.ya":
                    metodo="Efectivo P.ya"
                    break
            elif selection=="4":
                if self.tipo_de_precio=="p.ya":
                    metodo="Pago Online P.ya"
                    break
            elif selection=="F":
                if cajero.nivel_privilegio=="2":
                    metodo="Fiado"
                    break
            else:
                pass
        while True:
            visual.cls()
            visual.banner_pedido()
            visual.titulo("METODO DE PAGO",metodo)
            visual.confirmar()
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="1":
                self.metodo_de_pago=metodo
                escritor.cambiar_r2("logout")
                return "logout"
            elif selection=="2":
                escritor.cambiar_r2("pedido.establecer_metododepago()")
                break
            else:
                pass

    def vista_previa(self):
        while True:
            visual.cls()
            print("")
            visual.vista_previa_pedido()
            print("")
            print("________________________________________________________________________________")
            print("                   |   0    |           Volver              |")
            print("                    ----------------------------------------")
            selection=visual.prompt(cajero.nombre_cajero.capitalize())
            if selection=="0":
                return "logout"
            else:
                pass        
    


def buscador(nombres,codigos,modo="K"):
    resultados=list()
    busqueda=visual.prompt("Buscar")
    for nombre in nombres:
        if busqueda.lower() in nombre.lower():
            resultados.append(nombre)
        else:
            pass
    if modo=="corto":
        return resultados
    else:
        pass
    visual.menu("{} RESULTADOS".format(len(resultados)),resultados)
    selection=visual.prompt(cajero.nombre_cajero.capitalize())
    if selection=="0":
        return 0
    elif int(selection)<=len(resultados):
        return escritor.elegir_producto(codigos[nombres.index(resultados[int(selection)-1])])
    else:
        pass
    return 0
def main_loop():
    pedido.tipo_de_precio=pedido.establecer_tipoprecio()
    while True:
        visual.cls()
        visual.banner_pedido()
        visual.vista_previa_pedido_mainloop()
        visual.menu("MENU DE OPCIONES",["Modificar Productos","Modificar Info","Vista Previa","Marchar Pedido"])
        selection=visual.prompt(cajero.nombre_cajero.capitalize())
        if selection=="0":
            break
        elif selection=="1":
            r1=pedido.mod_productos()
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
        elif selection=="2":
            r1=pedido.mod_info()
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
        elif selection=="3":
            r1=pedido.vista_previa()
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
        elif selection=="4":
            pass
        else:
            pass
    

    
###DECLARACION DE AGENTES DEL FRONTEND
visual=Visual()
cajero=Cajero()
pedido=Pedido()
producto=Producto()
promo=Promo()



main_loop()