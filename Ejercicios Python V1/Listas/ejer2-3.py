'''
    2.3. Definir una lista por asignación que almacene en la primer componente el nombre
         de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el
         promedio de las dos notas.

'''

'''
    RESUELTO POR EL PROFE

alumno = ["juan", 4,7]
prom = (alumno[1] + alumno[2])/2
print(f'Nombre: {alumno[0]}\nPromedio: {prom}')

'''

alumno = ["juan",8, 10,5]
sumaNota=0
for x in range (1,len(alumno)):
    sumaNota = sumaNota + alumno[x]
promedio = sumaNota / (len(alumno)-1)
print(f'Nombre: {alumno[0]}\nPromedio: {promedio}')

