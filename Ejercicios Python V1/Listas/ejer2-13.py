'''
    2.13. Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
           Mostrar el nombre de persona menor en orden alfabético.

'''

lista = []
for x in range(0,5):
    nombre= input ("ingrese un nombre: ")
    lista.append(nombre)
lista.sort()
print("El primer nombre en orden alfabetico es: {}".format(lista[0]))