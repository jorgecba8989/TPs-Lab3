'''
    Confeccionar una función que le enviemos como parámetro un string y nos 
    retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga 
    de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque 
    principal cual de las dos palabras tiene más caracteres.
'''
def carga():
    pal1 = input("Ingrese una palabra: ")
    pal2 = input("Ingrese otra palabra: ")
    cantPal1 = contar(pal1)
    cantPal2 = contar(pal2)
    if cantPal1 > cantPal2:
        print ("La PRIMERA palabra ingresada tiene mas caracteres")
    else:
        print ("La SEGUNDA palabra ingresada tiene mas caracteres")

def contar(p):
    return len(p)


carga()