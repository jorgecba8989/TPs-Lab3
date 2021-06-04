'''
    1.6. Ingresar una oración que pueden tener letras tanto en mayúsculas como
        minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la
        oración en minúsculas para que sea más fácil disponer la condición que verifica que
        es una vocal.
'''
oracion = input("Ingresa una oracion: ")
oracion_minuscula=oracion.lower()
cantVocales=0
for x in oracion_minuscula:
     if x=="a" or x=="e" or x=="i" or x=="o" or x=="u": 
        cantVocales = cantVocales + 1
print(f'Hay {cantVocales} vocales en tu oracion') 