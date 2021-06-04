'''
    2.5. Definir una lista que almacene por asignación los nombres de 5 personas.
        Contar cuantos de esos nombres tienen 5 o más caracteres.

'''

nombres = ["victor", "ana", "luis", "mariana","maty"]
contar = 0
cantidad = 0
for x in range (0,len(nombres)):
    cantidad = len(nombres[x]) 
    if cantidad > 4:
        contar = contar + 1
print(f'Hay {contar} nombres que tienen 5 o mas caracteres')