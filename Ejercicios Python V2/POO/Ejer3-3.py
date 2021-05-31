'''
    Confeccionar una clase que represente un empleado. Definir como atributos 
    su nombre y su sueldo. En el método __init__ cargar los atributos por teclado y 
    luego en otro método imprimir sus datos y por último uno que imprima un 
    mensaje si debe pagar impuestos (si el sueldo supera a 3000).

'''

class Empleado:
    def __init__(self):
        self.nombre = input("Nombre del empleado: ")
        self.sueldo = int(input("Sueldo: "))

    def mostrar(self):
        print("\nNombre: ",self.nombre)
        print("Sueldo: ",self.sueldo)
    
    def control(self):
        if self.sueldo > 3000:
            return print ("Debe pagar impuestos")
        return print ("Cobra menos de 3000, por lo tanto no paga impuestos")


persona1=Empleado()
persona1.mostrar()
persona1.control()