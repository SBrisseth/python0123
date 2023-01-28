class Producto :
    def __init__(self,nombre,descripcion,marca,precio:float):
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = precio

    def __str__(self)->str:
        return f"{self.nombre}  {self.descripcion} S/ {self.precio}"

class Catalogo:
    listproductos = []
    
    def __init__(self, listproductos:list=[]):
        self.listproductos= listproductos

    def addProd(self, prod):  
        self.listproductos.append(prod)

    def listarProd(self):
        for i,prod in enumerate(self.listproductos):
            i=i+1
            print(i,prod)  # Print toma por defecto str(p)


# p1=Producto()
# p2=Producto()
listCatalogo = Catalogo()
# listCatalogo.addProd(p1)
# listCatalogo.addProd(p2)
# listCatalogo.listarProd()