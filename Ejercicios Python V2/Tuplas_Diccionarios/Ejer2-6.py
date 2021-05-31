'''
    Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha. 
    Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora 
    y la actividad). Implementar las siguientes funciones:
        1) Carga de datos en la agenda.
        2) Listado completo de la agenda.
        3) Consulta de una fecha.

'''

agenda = {}

def carga():
    otraFecha = "S"
    while otraFecha == "S":
        fe = input("Ingresa la fecha con el formato dd-mm-aaaa: ")
        otraAct = "S"
        hora_act = []
        while otraAct == "S":
            hora = input("Ingresa la hora con el formato hh:mm: ")
            act = input("Ingresa una actividad: ")
            hora_act.append((hora,act))
            otraAct = input ('''Subir otra actividad? 
                                \t S - Si
                                \t N - No 
                                \t\t Elija una opcion (S o N):  ''').upper()
        agenda[fe] = hora_act
        otraFecha = input("Ingresar otra fecha? (ingresar S o N): ").upper()
    return agenda


def mostrar(a):
    return print (a)


def buscarFecha(a):
    fechaIntroducida = input("Fecha a buscar (ingresar con formato dd-mm-aaaa): ")
    buscarF = a.get(fechaIntroducida)
    return print ("La feche",fechaIntroducida,"contiene",buscarF)

carga()
mostrar(agenda)
buscarFecha(agenda)