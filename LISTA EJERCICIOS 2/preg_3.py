a=int(input("ingrese 1er num:"))
b=int(input("ingrese 2do num:"))
  #definir una funcion que retorne el mayor valor al ingresar dos numeros
def mayor(a,b):
  if(a!=b):
    if a>b:
        print(str(a)+ ' es mayor que '+str(b))
    else:
      print(str(b)+ ' es mayor que '+str(a))

mayor(a,b)