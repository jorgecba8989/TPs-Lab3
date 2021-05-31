'''
    Desarrollar un programa que permita cargar 5 nombres de personas y sus 
    edades respectivas. Luego de realizar la carga por teclado de todos los datos 
    imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 
    años). Imprimir la edad promedio de las personas.

'''

def cargarPersona():
    listaP = []
    for x in range(2):
        nombreP = input('Ingrese nombre de la persona{0}: '.format(x))
        listaP.append(nombreP)
        edadP = int (input('Ingrese la edad de la persona{0}: '.format(x)))
        listaP.append(edadP)
    mayoresEdad(listaP)
    edadPromedio(listaP)

def mayoresEdad(l):
    mayoresEdad = []
    for x in range (1,len(l),2):
        if l[x] >= 18:
            mayoresEdad.append(l[x - 1])
    return print ("\nLos mayores o iguales a 18 son: ",mayoresEdad)


def edadPromedio(l):
    total = 0
    for x in range (1,len(l),2):
        total = total + l[x]
    prom = total / len(l)
    return print ("\nLa edad promedio es: ",prom)

cargarPersona()


'''
OTRA FORMA DE RESOLVERLO:

nombres = []
edades = []


def cargaDatosPlanilla(cantidad):
    for i in range(cantidad):
        nombre = input(f"Nombre {i+1}: ")
        nombres.append(nombre)

        edad = int(input(f"Ingrese edad {i+1}: "))
        edades.append(edad)


def verMayoresDeEdad():
    for i in range(len(edades)):
        if edades[i] >= 18:
            print(nombres[i]+f" ({edades[i]})")


def promedioEdades():
    promedio = sum(edades)/len(edades)
    respuestaPromedio = f"La edad promedio en la lista es de {promedio} años."
    print(respuestaPromedio)


cargaDatosPlanilla(2)
verMayoresDeEdad()
promedioEdades()

'''