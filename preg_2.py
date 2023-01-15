import math
print("PREGUNTA Nº2")

print("----------MENU-----------")
print(" 1. Area del circulo")
print(" 2. Area del rectangulo")
print(" 3. Area del triangulo")
print("-------------------------\n")
op = int(input("ingrese el area a calcular :"))
if(op == 1):
  radio = float(input("ingrese el radio del circulo:"))
  print("El area del circulo es : ",math.pi*pow(radio,2))
elif(op == 2):
  base = float(input("ingrese la base del rectangulo:"))
  altura = float(input("ingrese la altura del rectangulo:"))
  print("El area del rectangulo es : ",base*altura)
elif(op==3):
  base = float(input("ingrese la base del triangulo:"))
  altura = float(input("ingrese la altura del triangulo"))
  print("El area del triangulo es : ",(base*altura)/2)

print("--------------------------")