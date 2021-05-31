'''
    Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un 
    pais y la cantidad de habitantes. Definir tres funciones, en la primera cargar la 
    lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con 
    mayor cantidad de habitantes.

'''

def carga():
    paises = ()
    for x in range (2):
        a = input("Cargue un nombre del pais {0}: ".format(x))
        y = list(paises)
        y.append(a)
        paises = tuple(y)
        b = int (input("Cargue un valor {0}: ".format(x)))
        yy = list(paises)
        yy.append(b)
        paises = tuple(yy)
    mostrar(paises)
    pais_habitantes(paises)


def mostrar(p):
    return print ("\nLa tupla es -> ",p)


def pais_habitantes(p):
    mayor = 0
    for x in range (1,len(p),2):
        if p[x]> mayor:
            mayor = p[x]
            pais = p[x-1]
    return print ("\nEl pais ",pais,"tiene " ,mayor , " habitantes")
    

carga()
