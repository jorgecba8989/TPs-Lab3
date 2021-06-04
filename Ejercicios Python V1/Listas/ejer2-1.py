'''
2.1. Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar
     dicha suma.
'''
listaValores = [4,5,8,1433] #esto es una lista de asignacion
res=0

for x in listaValores:
    res = res + x

print("la suma de todos los valores es: {}".format(res))