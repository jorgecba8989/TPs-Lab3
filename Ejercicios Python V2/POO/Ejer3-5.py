'''
    Confeccionar una clase que administre una agenda personal. Se debe 
    almacenar el nombre de la persona, teléfono y mail. Debe mostrar un menú con 
    las siguientes opciones:
        1- Carga de un contacto en la agenda.
        2- Listado completo de la agenda.
        3- Consulta ingresando el nombre de la persona.
        4- Modificación de su teléfono y mail.
        5- Finalizar programa
'''

agenda = {}

class Agenda:
    def __init__(self):
        menu = 0
        while menu != '5':
            menu = input ('''\tElija una de las opciones!!! 
                                    \t 1 - Cargar datos para la agenda
                                    \t 2 - Mostrar la agenda
                                    \t 3 - Buscar persona
                                    \t 4 - Modificar telefono y mail
                                    \t 5 - Salir
                                    \t\t Opcion:  ''')
            if menu == "1":
                datos = []
                self.nombre = input("Nombre: ") 
                self.telefono = int(input("Telefono: "))
                self.mail = input("Email: ")
                datos.append((self.telefono,self.mail))
                agenda[self.nombre] = datos
            elif menu == "2":
                print (agenda)
            elif menu == "3":
                contacto = input("Nombre del contacto a buscar: ")
                buscarContacto = agenda.get(contacto)   
                print (buscarContacto)
            elif menu == "4":
                contacto = input("Nombre del contacto a modificar los datos: ")
                if contacto in agenda.keys():
                    self.telefono = int(input("Nuevo telefono: "))
                    self.mail = input("Nuevo email: ")
                    agenda[self.nombre] = (self.telefono,self.mail)
                    print ("Se actualizaron los datos")
                else: print ("No existe ese contacto...")


menu=Agenda()
