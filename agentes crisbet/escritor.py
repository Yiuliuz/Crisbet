class Escritor_Lector():
    def __init__(self):
        pass
    def crear_archivo_plano(ruta,texto):
        txt=open(ruta,"w")
        txt.write(str(texto))
        txt.close()
    def leer_archivo_plano(self,ruta):
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return texto
    def crear_archivo_turno(ruta,texto):
        txt=open(ruta,"w")
        txt.write(cesar.encriptar(texto),cesar.clave_turno)
        txt.close()
    def leer_archivo_turno(ruta):
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return cesar.desencriptar(texto,cesar.clave_turno)
    def crear_archivo_fijo(self,ruta,texto):
        clave=cesar.clave_fija
        txt=open(ruta,"w")
        txt.write(cesar.encriptar(texto,clave))
        txt.close()
    def leer_archivo_fijo(self,ruta):
        clave=cesar.clave_fija
        txt=open(ruta,"r")
        texto=txt.read()
        txt.close()
        return cesar.desencriptar(texto,clave)
    def cambiar_r2(self,texto):
        self.crear_archivo_fijo("{}\\r2.txt".format(operative_sist.ruta_temporales),texto)
    def obtener_r2(self):
        return self.leer_archivo_fijo("{}\\r2.txt".format(operative_sist.ruta_temporales))
    def cambiar_vbs(self,nombre):
        txt=open("{}/vbs/{}.txt".format(cesar.ruta_local,cesar.encriptar(nombre,cesar.clave_fija)),"r")
        encriptado=txt.read()
        txt.close()
        txt=open("{}/aux.vbs".format(cesar.ruta_temporales),"w")
        txt.write(cesar.desencriptar(encriptado,cesar.clave_fija))
        txt.close()