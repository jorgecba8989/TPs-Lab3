'''
    Definir por asignación una lista de enteros en el bloque principal del 
    programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de 
    todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última 
    recibe la lista y retorna el menor
'''

def lista():
    listaEnteros = [3,14,12,9]
    suma(listaEnteros)
    mayor(listaEnteros)
    menor(listaEnteros)

def suma(l):
    res = 0
    for x in l:
        res = res + x
    return print("La suma de la lista es: ",res)


def mayor(l):
    mayor= 0
    for x in range (len(l)):
       if l[x] > mayor:
            mayor = l[x]
    return print ("El mayor de la lista es: ",mayor)

def menor(l):
    menor = l[0]
    for x in range (len(l)):
       if l[x] < menor:
            menor = l[x]
    return print ("El menor de la lista es: ",menor)

lista()