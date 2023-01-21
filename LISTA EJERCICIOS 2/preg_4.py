import sys

def obtenerArgumentos(*args):
    nombre_script=sys.argv[0]
    arguments = list(args) 
    nuevo_script=[]
    nuevo_script.append(nombre_script)
    for i in range(len(arguments)):
        nuevo_script.append(arguments[i])
    return print(nuevo_script)

obtenerArgumentos(24,"clara","cobba")