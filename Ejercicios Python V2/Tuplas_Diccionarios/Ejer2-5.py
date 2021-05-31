'''
    Confeccionar un programa que permita cargar un código de producto como 
    clave en un diccionario. Guardar para dicha clave el nombre del producto, su 
    precio y cantidad en stock.
    Implementar las siguientes actividades:
        1) Carga de datos en el diccionario.
        2) Listado completo de productos.
        3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
        4) Listado de todos los productos que tengan un stock con valor cero
'''

productos = {}

def cargar():
    for x in range (1):
        a = input("Ingrese un producto: ")
        nombre = input("Ingrese el nombre: ")
        precio = int (input("Ingrese el precio: "))
        stock = int (input("Ingrese el stock: "))
        datos = {nombre,precio,stock}
        productos[a]=datos
    return productos


def mostrar(prod):
    return print ("\nLos productos son -> ",prod)


def buscarProducto(prod):
    buscarP = input("\nProducto a buscar: ")
    productoEncontrado = prod.get(buscarP)
    return print ("Se encontro -> ",productoEncontrado)


def stockCero(prod):
    for x in prod:
        if prod [x][2] == 0:
            print ("El producto con cero stock es ->",prod[x][0],prod[x][1], prod[x][2])

cargar()
mostrar(productos)
buscarProducto(productos)
stockCero(productos)