"""
recibes una sencuencia de numeros que puede ser una lista, tupla o incluso un generador, 
convierte la secuencia a una lista y retorna la lista de forma inversa
"""


def lista_inversa(n:int) -> list:
    return sorted(n, reverse=True)


#por que resolverlo de esta manera?
#sorted crea una lista a partir de cualquier objeto iterable, asi que como primer parametro le pasamos n
#luego le indicamos como queremos que cree esta lista, y le ponemos como segundo parametro reverse=True

numeros = (1, 2, 3, 6, 5, 4, 8, 151, 841, 5, 15, 1)
resultado = lista_inversa(numeros)
print(resultado)