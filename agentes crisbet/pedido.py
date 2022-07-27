class Pedido():
    def __init__(self,i):
        self.atributos=["ID","PRODUCTOS","METODO DE ENTREGA","METODO DE PAGO","TOTAL","HORA DE CONFIRMADO"]
        self.id=i
        self.turno=cajero.nombre_de_turno
        self.cajero=cajero.nombre_de_cajero
        self.fecha=operative_sist.obtener_fecha()
        self.productos=list()
        self.cantidad_productos=0
        self.subtotal=0
        self.total=0.0
        self.descuento=0.0
        self.recargo=0.0

        
    def añadir_producto(self,producto,cantidad):
        self.productos.append("{},{},{},{}".format(cantidad,producto[0],producto[1],producto[-1]))
    def eliminar_producto(self,producto):
        self.productos.pop(producto)
    def elegir_tipo_precio(self,tipo):
        self.tipo_precio=tipo
    def elegir_metodo_de_entrega(self,metodo_de_entrega):
        self.metodo_de_entrega=metodo_de_entrega
    def elegir_metodo_de_pago(self,metodo_de_pago):
        self.metodo_de_pago=metodo_de_pago
    def obtener_subtotal(self):
        for producto in self.productos:
            producto=producto.split(",")
            self.subtotal=self.subtotal+int(producto[0])*int(producto[2])
    def agregar_descuento(self,descuento):
        self.descuento=float(descuento)
    def agregar_recargo(self,recargo):
        self.recargo=float(recargo)
    def escribir_comanda(self):
        self.comanda="Pedido {}\n{}\n{}\n--------------------\n".format(self.id,self.metodo_de_entrega,self.hora_confirmacion)
        for producto in productos:
            codigo=producto[-1]
            if codigo[2]=="0":
                self.comanda=self.comanda+"{} {}\n".format(producto[0],producto[1])
            elif codigo[2:5]=="2-0":
                self.comanda=self.comanda+"{} {}\n".format(producto[0],producto[1])
            else:
                pass
        self.comanda=self.comanda+"--------------------\n"
    def escribir_ticket(self):
        self.ticket="{} {} {}\nPedido {}\n{}\nMetodo de pago {}\n--------------------\n".format(self.fecha,self.turno,self.cajero,self.id,self.metodo_de_entrega,self.metodo_de_pago)
        for producto in productos:
            producto=producto.split(",")
            self.ticket=self.ticket+"{} {} {}\n".format(producto[0],producto[1],producto[2])
        self.ticket=self.ticket+"--------------------\nSubtotal ${}\nDescuento ${}\nRecargo ${}\nTotal ${}\n--------------------".format(self.subtotal,self.descuento,self.recargo,self.total)
    def ver_comanda(self):
        self.hora_confirmacion=operative_sist.obtener_hora()
        self.escribir_comanda()
        return self.comanda
    def ver_pedido(self):
        self.hora_confirmacion=operative_sist.obtener_hora()
        self.obtener_subtotal()
        self.total=self.subtotal+self.recargo-self.descuento
        self.escribir_ticket
        return self.ticket
    def marchar(self):
        #crear carpeta del pedido en marchados
        operative_sist.crear_carpeta("{}\\pedido{}".format(cajero.ruta_marchando,self.id)
        #hora de confirmacion
        self.hora_confirmacion=operative_sist.obtener_hora()
        #subtotal
        self.obtener_subtotal()
        #total
        self.total=self.subtotal+self.recargo-self.descuento
        #cantidad de productos
        for producto in productos:
            self.cantidad_productos=self.cantidad_productos+int(producto[0])
        #atributos para el panel de control
        self.atributos[0]="Pedido "+self.id
        self.atributos[1]=str(self.cantidad_productos)+" Productos"
        self.atributos[2]=self.metodo_de_entrega
        self.atributos[3]=self.metodo_de_pago
        self.atributos[4]=self.total
        self.atributos[5]=self.hora_confirmacion
        #escribir ticket y comanda
        self.escribir_ticket()
        self.escribir_comanda()
        #escribir archivos de comanda, ticket y atributos en la carpeta marchados
        escritor.crear_archivo_turno("{}\\pedido{}\\ticket.txt".format(cajero.ruta_marchando,self.id),self.ticket)
        escritor.crear_archivo_turno("{}\\pedido{}\\comanda.txt".format(cajero.ruta_marchando,self.id),self.comanda)
        atributos_str=str()
        for atributo in self.atributos:
            if atributo==self.atributos[-1]
                atributos_str=atributos_str+atributo
            else:
                atributos_str=atributos_str+atributo+"\n"        
        escritor.crear_archivo("{}\\pedido{}\\atributos.txt".format(cajero.ruta_marchando,self.id))
        #imprimir comanda y ticket
        impresora.imprimir(self.comanda)
        input("IMPRIMIENDO COMANDA, pulse enter para imprimir ticket")
        impresora.imprimir(self.ticket)
        input("IMPRIMIENDO TICKET, pulse enter para imprimir ticket")
        #eliminar carpeta del pedido en armando
        operative_sist.eliminar_carpeta("{}\\pedido{}".format(cajero.ruta_armando,self.id))



