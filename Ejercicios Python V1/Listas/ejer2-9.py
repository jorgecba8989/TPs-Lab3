'''
    2.9. Obtener el promedio de las mismas. Contar cuántas personas son más altas que el
         promedio y cuántas más bajas.

'''
lista = []
valor= 0.0
sumaTotal = 0.0
promedio = 0.0
per_altos= 0
per_bajos= 0
for x in range(0,5):
    valor= float (input('Ingrese el valor de la posicion {0}: '.format(x)))
    lista.append(valor)
    sumaTotal = sumaTotal + lista[x] 
promedio = sumaTotal / len(lista)
for x in range (0,len(lista)):
    if lista[x] > promedio:
        per_altos = per_altos + 1
    else:
        per_bajos = per_bajos + 1
print(f'Promedio: {promedio}')
print(f'Personas altas al promedio: {per_altos}')
print(f'Personas bajas al promedio: {per_bajos}')