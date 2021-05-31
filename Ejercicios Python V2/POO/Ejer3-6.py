'''
    Plantear un programa que permita jugar a los dados. Las reglas de juego 
    son: se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje 
    que "gano", sino "perdió".
    Pistas: Lo primero importar random. Despues lo que hacemos es 
    identificar las clases: Dado y JuegoDeDados. 
    Luego los atributos y los métodos de cada clase:
        #Clase Dado :
            -atributos: valor
            -métodos: tirar, imprimir, retornar_valor
        #Clase JuegoDeDados:
            -atributos: 3 Dado (3 objetos de la clase Dado)
            -métodos: __init__, jugar
'''


import random

class Dado:

    def tirar(self):
        self.valor = random.randint(1, 6)
        return self.valor

    def imprimir(self):
        print (self.valor)

    def retornar_valor(self):
        return self.valor


class JuegoDeDados:
    def __init__(self):
        self.dado1= Dado()
        self.dado2= Dado()
        self.dado3= Dado()
    
    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        self.dado1.imprimir()
        self.dado2.imprimir()
        self.dado3.imprimir()
        if (self.dado1.retornar_valor() == self.dado2.retornar_valor() == self.dado3.retornar_valor()):
            return print ("Ganaste")
        else:
            return print ("Perdiste")


d=JuegoDeDados()
d.jugar()

