'''
        2.7. Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar
             la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

'''
lista = []
valor=int (input("Ingresa un valor, con cero termina la carga: "))
while valor != 0:
    lista.append(valor)
    valor=int (input("Ingresa otro valor, con cero termina la carga: "))
print(f'El tamanio de la lista es: {len(lista)}')

