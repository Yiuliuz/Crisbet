from os import getcwd


def elegir_producto_DB(codigo):
    ruta="{}//data//productos//{}".format(getcwd(),codigo)
    producto=list()
    ######setear datos del producto######
    txt=open("{}//nombre.txt".format(ruta),"r")
    nombre=txt.read()
    txt.close()
    producto.append(nombre)
    ######################################
    txt=open("{}//precio.txt".format(ruta),"r")
    precio=txt.read()
    txt.close()
    producto.append(precio)
    ######################################
    txt=open("{}//stock.txt".format(ruta),"r")
    stock=txt.read()
    txt.close()
    producto.append(stock)
    ######################################
    txt=open("{}//selection.txt".format(ruta),"r")
    selection=txt.read()
    txt.close()
    producto.append(selection)
    ######################################
    txt=open("{}//elementos.txt".format(ruta),"r")
    elementos=txt.read()
    txt.close()
    producto.append(elementos)
    ######################################
    txt=open("{}//codigo.txt".format(ruta),"r")
    codigo=txt.read()
    txt.close()
    ######################################
    if codigo[2]=="0":
        txt=open("{}//ingredientes.txt".format(ruta),"r")
        ingredientes=txt.read()
        txt.close()
        producto.append(ingredientes)
    else:
        pass
    ######################################
    producto.append(codigo)
    return producto



class Producto():
    def __init__(self,producto):
        self.nombre=producto[0]
        self.precio=producto[1]
        self.stock=producto[2]
        self.selection=producto[3]
        self.elementos=producto[4]
        self.codigo=producto[-1]
        if self.codigo[2]=="0":
            self.ingredientes=producto[5]
        else:
            pass
        

precio_tipo=input("Pedidos Ya o Local?")
if precio_tipo.lower()=="1":
    txt=open("{}//data//productos//nombres_pya.txt".format(getcwd()),"r")
    nombres=txt.read().split("\n")
    txt.close()
    txt=open("{}//data//productos//codigos_pya.txt".format(getcwd()),"r")
    codigos=txt.read().split("\n")
    txt.close()
elif precio_tipo.lower()=="2":
    txt=open("{}//data//productos//nombres_local.txt".format(getcwd()),"r")
    nombres=txt.read().split("\n")
    txt.close()
    txt=open("{}//data//productos//codigos_local.txt".format(getcwd()),"r")
    codigos=txt.read().split("\n")
    txt.close()

busqueda=input("Buscar: ")
resultados=list()
for nombre in nombres:
    nomb=nombre.lower()
    if busqueda.lower() in nomb:
        resultados.append(nombre)
    else:
        pass

x=1
for resultado in resultados:
    print(x,"-",resultado)
    x=x+1
selection=input("Elija:")
eleccion=resultados[int(selection)-1]
indice=nombres.index(eleccion)
codigo=codigos[indice]


producto=Producto(elegir_producto_DB(codigo))
print(producto.nombre)
for ingr in producto.ingredientes.split(","):
    print(ingr)