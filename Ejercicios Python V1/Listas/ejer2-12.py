''''
    2.12. Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que
            identifique el menor valor de la lista y la posición donde se encuentra.

'''
lista = []
valor= 0
for x in range(0,5):
    valor= int (input('Ingrese el valor de la posicion {0}: '.format(x)))
    lista.append(valor)
menor=lista[0]
posicion = 0
for x in range(0,5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = x
print(f'El menor de la lista es {menor} y estan el la posicion {posicion}')