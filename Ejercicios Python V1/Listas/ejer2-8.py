'''
    2.8. Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)

'''

lista = []
valor= 0.0
for x in range(0,5):
    valor= float (input('Ingrese el valor de la posicion {0}: '.format(x)))
    lista.append(valor)
print(f'La lista de Alturas: {lista}')