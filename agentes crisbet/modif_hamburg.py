def sacar_topings(hamburgesa):
    sacar=list()
    while True:
        ingredientes=hamburgesa[5]
        x=1
        for ingrediente in ingredientes:
            print(x," | ",ingrediente)
            x=x+1
        print("0 | Volver")
        print("00| Equivocación")
        selection=input("{}->".format(cajero.nombre_de_cajero))
        if selection=="0":
            return sacar
        elif selection=="00":
            sacar.pop()
        elif int(selection) <= len(ingredientes):
            sacar.append(ingredientes[int(selection)-1])
        else:
            pass
def agregar_topings(hamburgesa):

def modificar_hamburgesa(hamburgesa):
