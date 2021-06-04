'''
    2.11. Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el
            mayor valor de la lista.
'''
lista = []
valor= 0
mayor= 0
for x in range(0,5):
    valor= int (input('Ingrese el valor de la posicion {0}: '.format(x)))
    lista.append(valor)
    if lista[x] > mayor:
        mayor = lista[x]
print(f'El mayor de la lista es: {mayor}')
