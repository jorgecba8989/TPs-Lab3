'''
    En el bloque principal del programa definir un diccionario que almacene los 
    nombres de paises como clave y como valor la cantidad de habitantes. 
    Implementar una función para mostrar cada clave y valor.
'''

def mostrarPaises():
    paises= {
                "Argentina":"3000",
                "Colombia": "1200",
                "Brasil": "9800",
                "Chile" : "555" }
    a = input("Ingrese la clave: ")
    b = int (input("Ingrese el valor: "))
    paises[a]=b
    print ("El diccionario es ->",paises)


mostrarPaises()