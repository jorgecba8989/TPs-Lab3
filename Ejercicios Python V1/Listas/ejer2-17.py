'''
    2.17. Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento
            debe ser una lista de 5 enteros. Calcular y mostrar la suma de cada lista contenida en
            la lista principal.

'''
lista = [[1,2,3,4,5],[9,8,7,6,5]]
sub_lista1= 0
sub_lista2= 0
for x in range(0,2):
    sub_lista1 = sum(lista[0])
    sub_lista2 = sum(lista[1])
print(f'lista = [{sub_lista1},{sub_lista2}]')