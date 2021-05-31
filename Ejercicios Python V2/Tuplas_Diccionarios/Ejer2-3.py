'''
    Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el 
    nombre de productos y como valor el precio del mismo.
    Desarrollar además las funciones de:
        1) Imprimir en forma completa el diccionario
        2) Imprimir solo los artículos con precio superior a 100
'''

def articulos():
    articulos = {}
    for x in range (5):
        a = input("Ingrese la clave: ")
        b = int (input("Ingrese el valor: "))
        articulos[a]=b
    mostrar(articulos)
    mayoresA100(articulos)


def mostrar (a):
    return print (a)


def mayoresA100(a):
    for x in a:
        if a[x] > 100:
            print ("El producto",x," es mayores a 100 ")


articulos()