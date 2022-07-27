class Cesar():
    def __init__(self):
        self.ruta_local="{}\\data\\cesar\\local".format(getcwd())
        self.ruta_temporales="{}\\data\\cesar\\temp".format(getcwd())
        self.ruta_oculta="{}\\elvago".format(self.ruta_local)
        self.secuencia=self.obtener_secuencia_DB()
        self.clave_fija=self.obtener_clave_fija_DB()
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
            if contador==len(renglones):
                encriptado=encriptado+renglon_encriptado
            else:
                encriptado=encriptado+renglon_encriptado+"\n"
        return encriptado
    def desencriptar(self,encriptado,clave):
        renglones=encriptado.split("\n")
        desencriptado=str()
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
            if contador==len(renglones):
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