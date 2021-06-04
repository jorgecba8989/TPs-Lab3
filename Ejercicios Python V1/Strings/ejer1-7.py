'''
    1.7. Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de
        caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para que
        sea válido, en caso contrario mostrar un mensaje de error.

'''

clave = input ("Ingresa una clave entre 10 y 20 caracteres: ")
if len(clave) < 9 or len(clave) > 21:
    print("La clave ingresada NO es valida")
else:
    print("La clave es valida")