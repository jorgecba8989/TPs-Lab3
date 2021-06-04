'''
    1.2. Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si
                            comienza con vocal dicho nombre.

'''

nombre = input("Carga el nombre de una persona en minuscula: ")
if nombre[0]=="a" or nombre[0]=="e" or nombre[0]=="i" or nombre[0]=="o" or nombre[0]=="u":
    print(f'El nombre Si comienza con una vocal')
else:
    print(f'El nombre No comienza con una vocal')