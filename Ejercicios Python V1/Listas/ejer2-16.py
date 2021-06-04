'''
    2.16. Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a
             mayor la lista.

'''
lista = []
for x in range(5):
    val= int (input ("Ingrese un sueldo: "))
    lista.append(val)
lista.sort()
print("La lista esta ordenada de menor a mayor: {}".format(lista))