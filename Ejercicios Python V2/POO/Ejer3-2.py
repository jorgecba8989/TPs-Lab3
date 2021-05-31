'''
    Desarrollar un programa que cargue los lados de un triángulo e implemente 
    los siguientes métodos: inicializar los atributos, imprimir el valor del lado mayor y 
    otro método que muestre si es equilátero o no. El nombre de la clase llamarla 
    Triangulo.
'''

class Triangulo:
    def cargar(self,lado1,lado2,lado3):
        self.lado1 = lado1 
        self.lado2 = lado2
        self.lado3 = lado3

    
    def ladoMayor(self):
        if (self.lado1 > self.lado2) and (self.lado1 > self.lado3):
            return print ("Lado 1 es el mayor con valor",self.lado1)
        elif (self.lado2 > self.lado3):
            return print ("Lado 2 es el mayor con valor",self.lado2)
        else:
            return print ("Lado 3 es el mayor con valor",self.lado3)

    def equilatero(self):
        if (self.lado1 == self.lado2) and (self.lado1 == self.lado3):
            return print ("Es un triangulo equilatero")
        else:
            return print ("No es un triangulo equilatero")

triangulo=Triangulo()
triangulo.cargar(3,3,2)
triangulo.ladoMayor()
triangulo.equilatero()
