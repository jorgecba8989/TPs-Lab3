'''
        Supongamos que necesitamos implementar dos clases que llamaremos Suma y Resta. 
        Cada clase tiene como atributo valor1, valor2 y resultado. Los métodos a definir 
        son cargar1 (que inicializa el atributo valor1), carga2 (que inicializa el atributo valor2), 
        operar (que en el caso de la clase "Suma" suma los dos atributos y en el caso de la 
        clase "Resta" hace la diferencia entre valor1 y valor2), y otro método mostrar_resultado. 
        Si analizamos ambas clases encontramos que muchos atributos y métodos son idénticos. 
        En estos casos es bueno definir una clase padre que agrupe dichos atributos y responsabilidades comunes.

'''
class Control:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def carga1(self):
        self.valor1 = int(input("Ingrese el valor 1: "))

    def carga2(self):
        self.valor2 = int(input("Ingrese el valor 2: "))

    def operar(self):
        pass

    def mostrar_resultado(self):
        return print (self.resultado)



class Sumar(Control):
    
    def operar(self):
        self.resultado = self.valor1 + self.valor2


class Restar(Control):
    
    def operar(self):
        self.resultado = self.valor1 - self.valor2

print('SUMA')
suma=Sumar()
suma.carga1()
suma.carga2()
suma.operar()
suma.mostrar_resultado()

print('\nRESTA')
resta=Restar()
resta.carga1()
resta.carga2()
resta.operar()
resta.mostrar_resultado()