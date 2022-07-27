class Database():
    def __init__(self):
        self.ruta_temporales="{}\\data\\temp".format(getcwd())
        self.ruta_productos="{}\\data\\productos".format(getcwd())
    def elegir_producto_DB(self,codigo):
        ruta="{}\\{}".format(self.ruta_productos,codigo)
        producto=list()
        ######setear datos del producto######
        txt=open("{}\\nombre.txt".format(ruta),"r")
        nombre=txt.read()
        txt.close()
        producto.append(nombre)
        ######################################
        txt=open("{}\\precio.txt".format(ruta),"r")
        precio=txt.read()
        txt.close()
        producto.append(precio)
        ######################################
        txt=open("{}\\stock.txt".format(ruta),"r")
        stock=txt.read()
        txt.close()
        producto.append(stock)
        ######################################
        txt=open("{}\\selection.txt".format(ruta),"r")
        selection=txt.read()
        txt.close()
        producto.append(selection)
        ######################################
        txt=open("{}\\.txt".format(ruta),"r")
        =txt.read()
        txt.close()
        producto.append()
        ######################################
        txt=open("{}\\elementos.txt".format(ruta),"r")
        elementos=txt.read()
        txt.close()
        producto.append(elementos)
        ######################################
        txt=open("{}\\codigo.txt".format(ruta),"r")
        codigo=txt.read()
        txt.close()
        ######################################
        if codigo[2]=="0":
            txt=open("{}\\ingredientes.txt".format(ruta),"r")
            ingredientes=txt.read()
            txt.close()
            producto.append(ingredientes)
        else:
            pass
        ######################################
        producto.append(codigo)
        return producto