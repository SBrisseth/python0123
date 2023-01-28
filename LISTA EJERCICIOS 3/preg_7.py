class product:
    def __init__(self,nombre,codigo:str):
        self.nombre = nombre
        self.codigo = codigo
    def __str__(self):
        pais_orig = self.codigo[:self.codigo.index('-')]
        num_lote =  self.codigo[self.codigo.index('-')+1:len(self.codigo)-self.codigo.index('-')-1]
        return f"{self.nombre} \n" +"Pais de Origen :" + str(pais_orig) + "\nNumero Lote :" + str(num_lote)

