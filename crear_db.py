from os import getcwd
import os

ruta="C:\\Users\\Usuario\\Documents\\proyectos\\crisbet\\data\\productos"


precios=["Local","Pedidos Ya"]
archivos=["precio","elementos","selection","stock"]

nombres_local=open("nombres_local.txt","w")
codigos_local=open("codigos_local.txt","w")
nombres_pya=open("nombres_pya.txt","w")
codigos_pya=open("codigos_pya.txt","w")

txt=open("tipos.txt","r")
tipos=txt.read().split("\n")
txt.close()

txt=open("variedades.txt","r")
varies=txt.read().split("\n")
txt.close()

txt=open("tamaños.txt","r")
tams=txt.read().split("\n")
txt.close()





indice_tamaño=0

codigo_precio=0
indice_precio=0
for precio in precios:
    codigo_tipo=0
    indice_tipo=0
    indice_variedad=0
    for tipo in tipos:
        variedades=varies[indice_tipo].split(",")
        codigo_variedad=0
        for variedad in variedades:
            tamaños=tams[indice_variedad].split(",")
            codigo_tamaño=0
            for tamaño in tamaños:
                codigo="{}-{}-{}-{}".format(codigo_precio,codigo_tipo,codigo_variedad,codigo_tamaño)
                os.system("MKDIR {}\\{}".format(ruta,codigo))
                for archivo in archivos:
                    txt=open("{}\\{}\\{}.txt".format(ruta,codigo,archivo),"w")
                    txt.close()
                txt=open("{}\\{}\\nombre.txt".format(ruta,codigo),"w")
                txt.write(tamaño)
                txt.close()
                txt=open("{}\\{}\\stock.txt".format(ruta,codigo),"w")
                txt.write("SI")
                txt.close()
                if precio=="Local":
                    nombres_local.write("{}\n".format(tamaño))
                    codigos_local.write("{}\n".format(codigo))
                else:
                    nombres_pya.write("{}\n".format(tamaño))
                    codigos_pya.write("{}\n".format(codigo))
                codigo_tamaño=codigo_tamaño+1
            indice_variedad=indice_variedad+1
            codigo_variedad=codigo_variedad+1
        indice_tipo=indice_tipo+1
        codigo_tipo=codigo_tipo+1
    indice_precio=indice_precio+1
    codigo_precio=codigo_precio+1

nombres_local.close()
codigos_local.close()
nombres_pya.close()
codigos_pya.close()