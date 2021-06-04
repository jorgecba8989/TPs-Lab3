'''
        2.15. Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor
                mayor de la lista a la última posición.

'''
lista = []
for x in range(0,5):
    sueldo= int (input ("Ingrese un sueldo: "))
    lista.append(sueldo)
for x in range(0,4): 
    if lista[x] > lista[x + 1]:
        aux = lista[x]
        lista[x] = lista[x + 1]
        lista[x + 1] = aux
print(lista)