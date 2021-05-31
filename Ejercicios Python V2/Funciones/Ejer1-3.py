'''
    Confeccionar una función que reciba tres enteros y nos muestre el mayor de 
    ellos. La carga de los valores hacerlo por teclado.

'''

def mayor ():
    a=int (input("Ingrese primer valor: "))
    b=int (input("Ingrese segundo valor: "))
    c=int (input("Ingrese tercer valor: "))
    if (a > b) and (a > c):
        return print ("\t El mayor es ",a)
    elif (b > a) and (b > c):
        return print ("\t El mayor es ",b)
    else:
        return print ("\t El mayor es ",c)

mayor()