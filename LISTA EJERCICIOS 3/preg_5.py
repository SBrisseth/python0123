def suma_n(num:int)->int:
    if num ==1:
            return 1
    else:
        return num + suma_n(num-1)

def dividir(num1:float,num2:float)->float:
    if(num1!=0 and num2!=0):
        div = num1/num2
    return div

