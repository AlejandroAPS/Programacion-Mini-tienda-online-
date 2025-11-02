
#Importación lanzapapeadas
import Funciones_Articulos
import Funciones_Usuarios
import Funciones_Carrito

    # Listas para almacenar datos
articulos = []
usuarios = []
carrito = []
historialventas = []
menu_actual = "articulos"
usuario_seleccionado = None

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
                return ("usuarios")
            case 7:
                return ("carrito")
            case 8:
                return("salir")
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
                return "articulos"
            case 7:
                return "carrito"
            case 8:
                return "salir"
            case _:
                print("Por favor, escoge una opción válida.")

def menu_carrito():
    opcion = 0
    while opcion != 10:
        Funciones_Carrito.menu_carrito()
        opcion = int(input("Escoge el número de la opción que desees: "))
        match opcion:
            case 1:
                Funciones_Carrito.selecc_usuario1(usuarios, usuario_seleccionado)
            case 2:
                Funciones_Carrito.anadir_articulo2(articulos, carrito)
            case 3:
                Funciones_Carrito.borrararticulo3(carrito)
            case 4:
                Funciones_Carrito.vercarrito4(carrito)
            case 5:
                Funciones_Carrito.terminar_compra5(carrito, historialventas, usuario_seleccionado)
            case 6:
                print("opcion 6")
            case 7:
                Funciones_Carrito.vaciarcarrito7(carrito)
            case 8:
                return "articulos"
            case 9:
                return "usuarios"
            case 10:
                return "salir"
            case _:
                print("Por favor, escoge una opción válida.")

    #A partir de aqui empieza la logica del programa
while True:
    if menu_actual == "articulos":
        print("Cargando gestión de artículos...")
        menu_actual = menu_articulos()
    elif menu_actual == "usuarios":
        print("Cargando gestión de usuairos")
        menu_actual = menu_usuarios()
    elif menu_actual == "carrito":
        print("Cargando carrito")
        menu_actual = menu_carrito()
    elif menu_actual == "salir":
        print("Saliendo del programa...")
        exit()




