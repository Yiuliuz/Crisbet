#clase para el panel de control, recibe 3 parametros: una lista con
#los atributos id,cantidad productos,metodo de entrega,metodo de
#pago, total y hora de confirmacion. un str que es el ticket, y un str
#que es la comanda
class Pedido_Marchado():
    def __init__(self,atributos,ticket,comanda):
        self.ticket=ticket
        self.comanda=comanda
        self.id=atributos[0]
        self.cantidad_productos=atributos[1]
        self.metodo_de_entrega=atributos[2]
        self.metodo_de_pago=atributos[3]
        self.total=atributos[4]
        self.hora_confirmacion=atributos[5]
