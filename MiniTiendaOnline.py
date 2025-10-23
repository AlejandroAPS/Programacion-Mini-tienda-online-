##Variables
opcion = 0
articulos = []
##Funciones
#Definicion del menu
def menu():             
    print("1.Crear artículo")
    print("2.Listar artículos")
    print("3.Buscar artículos por id")
    print("4.Actualizar artículo")
    print("5.Eliminar artículo")
    print("6.Alternar Activo/Inactivo")
    print("7.Salir")
#Definicion para crear un articulo nuevo
def crear1(nuevoarticulo):
    nuevonombre = str(input("Dime el nombre del producto a añadir:"))
    nuevoarticulo.update({"ID": len(articulos) + 1, "nombre": nuevonombre})
    nuevoprecio = float(input("Que precio va a tener?:"))
    nuevoarticulo.update({"precio": nuevoprecio })
    nuevostock = int(input("Que tanto stock hay?:"))
    nuevoarticulo.update({"stock": nuevostock })
    nuevoactividad = bool(input("Se puede vender ya mismo?:"))
    nuevoarticulo.update({"activo": nuevoactividad })
    articulos.append(nuevoarticulo)
    return articulos
#Definicion para mostrar todos los articulos ingresados por el usuario
def mostrar2():
    print(articulos)
#Definicion para buscar por ID de articulo
def buscar3(busqueda):
    if busqueda < len(articulos) + 1:
        for articulo in articulos:
            if articulo ["ID"] == busqueda:
                print(articulo)
    else:
        print("Artículo no encontrado")
#Definicion para actualizar los articulos(diccionarios) en la lista de articulos
def actualizar4()
    #toca tocar cosas por aqui xddddd

##Desarrollo Programa

menu()
while opcion != 7:
    opcion = int(input("Escoge el número de la opción que desees"))
    match opcion:
        case 1:
            crear1(nuevoarticulo = {})
        case 2:
            mostrar2()
        case 3:
            busqueda = int(input("Dime el ID numerico:"))
            buscar3(busqueda)
        case 4:
            print("opcion4")
        case 5:
            print("opcion5")
        case 6:
            print("opcion6")
        case 7:
            print("Terminando programa....")
        case _:
            print("opcion otro")