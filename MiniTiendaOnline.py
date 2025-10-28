import Funciones_Articulos
import Funciones_Usuarios
import Funciones_Carrito

# Listas para almacenar datos
articulos = []
usuarios = []

def menu_articulos():
    opcion = 0
    while opcion != 8:
        Funciones_Articulos.menu_articulos()
        opcion = int(input("Escoge el número de la opción que desees: "))
        
        match opcion:
            case 1:
                Funciones_Articulos.crear1(articulos)
            case 2:
                Funciones_Articulos.mostrar2(articulos)
            case 3:
                busqueda = int(input("Dime el ID numérico: "))
                Funciones_Articulos.buscar3(articulos, busqueda)
            case 4:
                Funciones_Articulos.actualizar4(articulos)
            case 5:
                Funciones_Articulos.borralacuenta5(articulos)
            case 6:
                print("Cargando gestión de usuarios...")
                menu_usuarios()  
            case 7:
                print("Cargando carrito...")
                menu_carrito()
            case 8:
                print("Saliendo del programa...")
                exit()    
            case _:
                print("Por favor, escoge una opción válida.")

def menu_usuarios():
    opcion = 0
    while opcion != 8:
        Funciones_Usuarios.menu_usuarios()
        opcion = int(input("Escoge el número de la opción que desees: "))

        match opcion:
            case 1:
                Funciones_Usuarios.crear1(usuarios)
            case 2:
                Funciones_Usuarios.mostrar2(usuarios)
            case 3:
                busqueda = int(input("Dime el ID numérico: "))
                Funciones_Usuarios.buscar3(usuarios, busqueda)
            case 4:
                Funciones_Usuarios.actualizar4(usuarios)
            case 5:
                Funciones_Usuarios.borralacuenta5(usuarios)
            case 6:
                print("Cargando gestión de artículos...")
                menu_articulos()
            case 7:
                print("Cargando carrito...")
                menu_carrito()
            case 8:
                print("saliendo del programa")
                exit()
            case _:
                print("Por favor, escoge una opción válida.")

def menu_carrito():
    opcion = 0
    while opcion != 10:
        Funciones_Carrito.menu_carrito()
        opcion = int(input("Escoge el número de la opción que desees: "))

        match opcion:
            case 1:
                print("Opcion 1")
            case 2:
                print("Opcion 2")
            case 3:
                print("Opcion 3")
            case 4:
                print("Opción 4")
            case 5:
                print("Opcion 5")
            case 6:
                print("opcion 6")
            case 7:
                print("Opcion 7")
            case 8:
                print("Cargando gestión de artículos...")
                menu_articulos()
            case 9:
                print("Cargando gestión de usuarios...")
                menu_usuarios()
            case 10:
                print("Saliendo del programa...")
                exit()
            case _:
                print("Por favor, escoge una opción válida.")


# 🔹 Aquí arranca todo el programa
menu_articulos()
