'''
    Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego 
    preguntar si quiere calcular y mostrar su perímetro o su superficie.
'''

def carga():
    a=int (input("Ingrese un valor: "))
    eleccion = input('''Desea calcular perimetro o superficie del cuadrado? \n 
                        \t 1 - Perimetro 
                        \t 2 - Superficie 
                        \t\t Elija una opcion: ''')
    if eleccion == "1":
        perimitro(a)
    if eleccion == "2":
        superficie(a)


def perimitro(lado):
    per = lado + lado + lado + lado
    return print ("\nEl perimetro del cuadrado es: " , per)

def superficie(lado):
    sup = lado * lado
    return print ("\nLa superficie del cuadrado es: " , sup)

carga()