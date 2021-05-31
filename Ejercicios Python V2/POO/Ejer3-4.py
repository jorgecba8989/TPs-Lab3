'''
    Desarrollar una clase que represente un punto en el plano y tenga los 
    siguientes métodos: inicializar los valores de x e y que llegan como parámetros, 
    imprimir en que cuadrante se encuentra dicho punto (concepto matemático, 
    primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.).

'''

class Plano:
    def inicializar (self,puntoX,puntoY):
        self.puntoX = puntoX 
        self.puntoY = puntoY

    def cuadrante(self):
        if (self.puntoX > 0) and (self.puntoY > 0):
            return print ("Esta en el primer cuadrante")
        elif (self.puntoX < 0) and (self.puntoY > 0):
            return print ("Esta en el segundo cuadrante")
        elif (self.puntoX < 0) and (self.puntoY < 0):
            return print ("Esta en el tercero cuadrante")
        else:
            return print ("Esta en el cuarto cuadrante")


puntos=Plano()
puntos.inicializar(-2,5)
puntos.cuadrante()