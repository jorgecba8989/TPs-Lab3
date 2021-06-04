'''
    2.4. Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos
        valores almacenan un valor superior a 100.
'''
listaNumeros = [20,120,80,30,300,150,90,105]
mayorCien = 0
posicion = 0 
for x in range (0,len(listaNumeros)):
    if listaNumeros[x] > 100:
        mayorCien = mayorCien + 1
print(f'Son {mayorCien} valores que superan los 100....')