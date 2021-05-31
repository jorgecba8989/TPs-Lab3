'''
    Confeccionar una aplicación que muestre una presentación en pantalla del 
    programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar 
    finalmente un mensaje de despedida del programa.
    Implementar estas actividades en tres funciones.

'''

def intro ():
    print ("*************************")
    print ("*                       *")
    print ("*   SUMA DE 2 NUMEROS   *")
    print ("*                       *")
    print ("*************************")

def suma ():
    a=int (input("Ingrese primer valor: "))
    b=int (input("Ingrese segundo valor: "))
    return print ("\t Total= ",a + b)

def despedida():
    print ("\t\nGracias, vuelva pronto....")

intro()
suma()
despedida()