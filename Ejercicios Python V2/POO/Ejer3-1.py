'''
    Implementar una clase llamada Alumno que tenga como atributos su nombre 
    y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar 
    un mensaje si está regular (nota mayor o igual a 4)

'''

class Alumno:
    def inicializar (self,nombre,nota):
        self.nombre = nombre 
        self.nota = nota

    def mostrar(self):
        return print ("El alumno",self.nombre,"saco" , self.nota)
    
    def regular(self):
        if self.nota >= 4:
            return print ("El alumno esta regular")
        else:
            return print ("El alumno vuelve en diciembre")

alumno1=Alumno()
alumno1.inicializar("Maty",5)
alumno1.mostrar()
alumno1.regular()