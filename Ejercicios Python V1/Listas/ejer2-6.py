'''
    2.6. Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a
         la lista. Imprimir la lista generada.

'''
lista = []
valor= 0
for x in range(0,5):
    #valor = input(f'Ingrese el valor de la posicion {x}:')     esto funciona
    valor=input('Ingrese el valor de la posicion {0}:'.format(x))
    lista.append(valor)
print(f'La lista con valores es: {lista}')