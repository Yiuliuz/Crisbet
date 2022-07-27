
cuentas=escritor.leer_archivo_fijo("{}\\elvago\\accounts.txt".format(getcwd())).split("\n")
usuario=input("Usuario: ")



def comprobar_cuenta(usuario,contraseña)
    acceso=False
    privilegios=0
    for cuenta in cuentas:
        acc=cuenta.split(",")
        if acc[0]==usuario:
            if acc[1]==contraseña:
                acceso=True
                privilegios=int(acc[2])
            else:
                pass
        else:
            pass
    return [acceso,privilegios]


