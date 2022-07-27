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
        

info=["nombre",100,True,"selection1_x()","Pan,Cheddar","Rucula,Tomate","0-0-0-0"]
hambr=Producto(info)
print(hambr.nombre[0])