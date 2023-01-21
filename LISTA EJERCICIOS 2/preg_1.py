mensaje="""Elija una de las siguientes opciones:
Seleccione 1 para la pregunta 1    
Seleccione 2 para la pregunta 2
Seleccione 3 para la pregunta 3"""
print(mensaje)
mensaje=int(input("ingrese la pregunta:"))
if mensaje==1:
  #dibujar un cuadrado
    n=int(input("ingrese el lado del cuadrado: "))
    for i in range(1,n+1):
      for j in range (1,n+1):
        print('*',end='')
      print('')
elif mensaje==2:
  #definimos una lista
    n=int(input("cuantos elementos tiene la lista:"))
    list1=[]
    for i in range(n):
      items = int(input("ingrese los elementos de la lista:"))
      list1.append(items)
    print(list1)
    for i in range (len(list1)):
      if list1[i]%2==0:
        print('el numero '+ str(list1[i])+ ' es par')
      else:
        print('el numero '+ str(list1[i])+ ' es impar')
elif mensaje==3:
    p=[]
    nombres= []
    edad = []
    n=int(input("ingrese la cantidad de datos a ingresar:"))
    for j in range(n):
      name=input("ingreses los nombres:")
      anio=int(input("ingrese las edades:"))
      nombres.append(name)
      edad.append(anio)    
    for i in range(len(nombres)):
      p.append([nombres[i],edad[i]])
      if(edad[i]>18):
        print(p[i])