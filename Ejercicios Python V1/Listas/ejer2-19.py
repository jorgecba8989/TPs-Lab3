'''
        2.19. Se tiene la siguiente lista:
                lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
                Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10
                contenidos en todos los elementos de la variable "lista". Volver a imprimir la lista.
'''

lista =  [[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
valor= 0
for i in range(len(lista[0])):
    for j in range(len(lista[i])):
        valor = lista[i][j]
        if valor > 10:
            lista[i][j] = 0
 
print (lista)