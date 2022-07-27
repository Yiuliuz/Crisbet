"""
Buscador: Recibe una lista de diccionarios como base de datos.
[{"nombre":"uno"},{"nombre":"dos"},{"nombre":"tres"}]
y una busqueda: "o" si la busqueda se encuentra en el valor "nombre" de un diccionario, este se agrega a la 
lista de resultados.
"""





def buscador(datos,busqueda):
    resultados=[]
    for elemento in datos:
        if busqueda in elemento["nombre"]:
            resultados.append(elemento)
    return resultados













from os import getcwd
######CARGAR Base de datos, pya o local
if precio_tipo()=="pya":
    txt=open("{}//data//productos//nombres_pya.txt".format(getcwd()),"r")
    nombres=txt.read().split("\n")
    txt.close()
    txt=open("{}//data//productos//codigos_pya.txt".format(getcwd()),"r")
    codigos=txt.read().split("\n")
    txt.close()
elif precio_tipo()=="local":
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
##imprimir resultados
for resultado in resultados:
    print(x,"-",resultado)
    x=x+1


selection=input("Elija:")

eleccion=resultados[int(selection)-1]
indice=nombres.index(eleccion)
codigo=codigos[indice]#asi se obtiene el codigo


