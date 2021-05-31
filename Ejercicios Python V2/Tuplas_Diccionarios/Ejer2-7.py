'''
    Confeccionar una función que reciba una palabra y verifique si es capicúa (es
    decir que se lee igual de izquierda a derecha que de derecha a izquierda).

'''

def cargar():
    palabra = input("Ingrese una palabra: ")
    inc = 0
    des = len(palabra)-1
    capicua = True
    while (inc < des) and (capicua !=False):
        if palabra[inc] == palabra[des]:
            inc = inc + 1
            des = des - 1
        else:
            capicua = False
    if capicua == True:
        return print ("La palabra",palabra," Si es capicua")
    else:
        return print ("La palabra",palabra," No es capicua")


cargar()
