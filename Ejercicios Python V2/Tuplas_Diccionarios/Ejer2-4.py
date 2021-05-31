'''
    Desarrollar una aplicación que nos permita crear un diccionario 
    ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en 
    castellano.
    Crear las siguientes funciones:
        1) Cargar el diccionario.
        2) Listado completo del diccionario.
        3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.
'''
palabras = {}

def cargar():
    for x in range (2):
        a = input("Ingrese la clave: ")
        b = input("Ingrese el valor: ")
        palabras[a]=b
    return palabras


def mostrar (a):
    return print (a)


def buscarPalabra(a):
    buscarP = input("Palabra a buscar: ")
    palabraTraducida = a.get(buscarP)
    return print ("La palabra",buscarP,"es",palabraTraducida)



cargar()
mostrar(palabras)
buscarPalabra(palabras)