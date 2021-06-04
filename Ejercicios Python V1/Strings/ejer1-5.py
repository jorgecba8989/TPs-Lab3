'''
    1.5. Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
         ingresaron. Tener en cuenta que un espacio en blanco es igual a " ", en cambio una
         cadena vacía es "".
'''
texto = input("Cargar una oracion: ")
cantidad = texto.count(" ")

print(f'Cantidad de espacios: {cantidad}')