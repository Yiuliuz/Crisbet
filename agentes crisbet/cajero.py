class Cajero():
    def __init__(self,nombre,privilegio):
        self.nivel_privilegio=privilegio
        self.nombre_de_cajero=nombre
    def iniciar_turno(self,numero):
        if len(listdir("{}\\data\\temp\\current".format(getcwd()))) >> 0:
            print("YA HAY UN TURNO INICIADO")
        else:
            self.numero_de_turno=str(numero)
            self.nombre_de_turno="{}-turno{}".format(operative_sist.obtener_fecha_numeros(),self.numero_de_turno)
            self.ruta_turno="{}\\data\\temp\\current\\{}".format(getcwd(),self.nombre_de_turno)
            self.ruta_retirados="{}\\retirados".format(self.ruta_turno)
            self.ruta_armando="{}\\armando".format(self.ruta_turno)
            self.ruta_marchando="{}\\marchando".format(self.ruta_turno)
            operative_sist.crear_carpeta(self.ruta_turno)
            operative_sist.crear_carpeta(self.ruta_armando)
            operative_sist.crear_carpeta(self.ruta_marchando)
            operative_sist.crear_carpeta(self.ruta_retirados)
    def continuar_turno(self):
        pass
    def terminar_turno(self):
        operative_sist.crear_carpeta("{}\\data\\local\ventas\\turnos\\{}".format(getcwd(),self.nombre_de_turno))
        operative_sist.copiar_archivo(self.ruta_retirados,"{}\\data\\local\\ventas\\turnos\\{}".format(getcwd(),self.nombre_de_turno))
        operative_sist.eliminar_carpeta(self.ruta_turno)