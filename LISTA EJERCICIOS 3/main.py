from preg_2 import *
from preg_3 import *
from preg_4 import *
from preg_5 import *
from preg_7 import *

def main():
# ___________________
    metodos(text)
# ____________________
    print(f1(3))
# ______________________
    p1=Producto('BATERIA','12V 55AH','RA',588)
    listCatalogo.addProd(p1)  
    listCatalogo.listarProd()
# __________________
    print(suma_n(4))
    print(dividir(40,2)) 
# __________________
    p3=product('TOYOTA','PERU-0001-2023')
    print(p3)

if __name__ == '__main__':
    main() 



