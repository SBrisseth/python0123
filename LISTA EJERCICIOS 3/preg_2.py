#Realizar un programa que realice las siguientes funciones
# de string al texto

text= """
    Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
    Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) 
    desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
        """

def metodos(text):#metodo split
    return print(text.split(),"\n","%".join(text),"\n",text.count("las"),"\n",text.find("libro"),"\n",text.upper(),"\n",text.lower())


