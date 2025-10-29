#Definicion del menu
def menu_carrito():             
    print("1.Seleccionar usuario activo")
    print("2.Añadir artículo al carrito")
    print("3.Quitar atículos del carrito")
    print("4.Ver carrito (detalle y total)")
    print("5.Confirmar compra (resta stock y registra venta)")
    print("6.Historial de ventas")
    print("7.Vaciar carrito")
    print("8.Menú gestión de artículos")
    print("9.Menú gestión de usuarios")
    print("10.Salir del programa")

#Definicion para escoger un usuario

def selecc_usuario1(usuarios, usuario_seleccionado):

    usuario_encontrado = False    #Esto es importante luego
    usuario_seleccionado = str(input("¿Cual es el nombre del artículo a actualizar?: "))
    for usuario in usuarios:
        if usuario["nombre"] == usuario_seleccionado:
            usuario_encontrado = True
            print("El usuario ha cambiado a: ", usuario_seleccionado)

    if usuario_encontrado == False:
        print("Usuario no encontrado")
        
    return usuario_seleccionado

def anadir_articulo2(articulos, carrito):
    articulo_encontrado = False    #Esto es importante luego
    nombre_articulo = str(input("¿Cual articulo quieres añadir al carrito?: "))
    for objeto in articulos:
        if objeto["nombre"] == nombre_articulo:
            articulo_encontrado = True
            carrito.append(objeto)  #Actualiza aqui el carrito con el articulo seleccionado
            print("Artículo añadido: ", objeto)
    if articulo_encontrado == False:
        print("Artículo no encontrado")
    return carrito
