'''
    2.18. Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento
            debe ser una lista, la primera lista tiene que tener un elemento, la segunda dos
            elementos, la tercera tres elementos y así sucesivamente. Sumar todos los valores de
            las listas.

'''
lista = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
sub_lista1= []
posicion = 0
for x in range(0,len(lista)):
    sub_lista1.append(sum(lista[x])) 
print(f'lista = {sub_lista1}')