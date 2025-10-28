##Variables / imports
import Funciones_Articulos
opcion = 0
articulos = []
##Desarrollo Programa
Funciones_Articulos.menu_articulos()
while opcion != 6:
    opcion = int(input("Escoge el número de la opción que desees"))
    match opcion:
        case 1:
            Funciones_Articulos.crear1(articulos)
        case 2:
            Funciones_Articulos.mostrar2(articulos)
        case 3:
            busqueda = int(input("Dime el ID numerico:"))
            Funciones_Articulos.buscar3(articulos, busqueda)
        case 4:
            Funciones_Articulos.actualizar4(articulos)
        case 5:
            Funciones_Articulos.borralacuenta5(articulos)
        case 6:
            print("Continuar a menu gestion de usuarios")
        case _:
            print("Porfavor escoga una opción de entre la lista")