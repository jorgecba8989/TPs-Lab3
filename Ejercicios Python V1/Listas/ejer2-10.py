'''
    2.10. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
            (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar
            los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.
'''
lista1 = []
lista2 = []
for x in range (0,4):
    turnoM= int (input ("Sueldo turno maniana: "))
    lista1.append(turnoM)
for x in range (0,4):
    turnoT= int (input ("Sueldo turno tarde: "))
    lista2.append(turnoT)
print(f'lista sueldo maniana: {lista1}  -   lista sueldo tarde: {lista2}')