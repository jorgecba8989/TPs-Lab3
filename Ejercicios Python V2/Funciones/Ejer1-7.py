'''
    Confeccionar una función que cargue por teclado una lista de 5 enteros y la 
    retorne. Una segunda función debe recibir una lista y mostrar todos los valores 
    mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.

'''

def principal():
    listaOb = cargaLista() 
    '''print (listaOb)'''
    mayor10(listaOb)
    
    
def cargaLista():
    lista = []
    for x in range(0,5):
        l = int (input('Ingrese el valor de la posicion {0}: '.format(x)))
        lista.append(l)
    return lista

def mayor10(l):
    listaN= []
    for x in range (len(l)):
       if l[x] > 10:
            listaN.append(l[x])
    return print ("Mayores a 10: ",listaN)


principal()