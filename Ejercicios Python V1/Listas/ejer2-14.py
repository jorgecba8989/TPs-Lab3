'''
        2.14. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se
                repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en
                la lista)
'''
lista = []
valor= 0
mayor= 0
repite = 0 
for x in range(0,5):
    valor= int (input('Ingrese el valor de la posicion {0}: '.format(x)))
    lista.append(valor)
    if lista[x] > mayor:
        mayor = lista[x]
for x in range (0,len(lista)):
    if lista[x] == mayor:
        repite = repite + 1
if repite > 1: 
    print(f'El mayor de la lista es {mayor} y se repite {repite}')
else:
    print(f'El mayor de la lista es {mayor}')