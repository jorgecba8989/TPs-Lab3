'''
        1.3. Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter
                            "@". Mostrar un mensaje informando dicha condición.

'''

email = input ("Ingrese un email: ")

if "@" in email:
    print("El email ingresado contiene el '@' ")
else:    
    print("El email no contiene '@' ")