'''
    Confeccionar una aplicación que solicite la carga de dos valores enteros y 
    muestre su suma. Repetir la carga e impresión de la suma 5 veces. Mostrar una 
    línea separadora después de cada vez que cargamos dos valores y su suma.

'''

def suma ():
    for x in range (5):
        print("Repeticion numero: ", x)
        a=int (input("Ingrese primer valor: "))
        b=int (input("Ingrese segundo valor: "))
        print ("\t Total= ",a + b)
        x = x + 1
        print("__________________________")
    return 0

suma()