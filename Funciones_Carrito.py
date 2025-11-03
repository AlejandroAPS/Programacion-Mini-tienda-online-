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
    usuario_seleccionado = str(input("¿Cual es el nombre del ususario a seleccionar?: "))
    for usuario in usuarios:
        if usuario["nombre"] == usuario_seleccionado:
            usuario_encontrado = True
            if usuario["activo"] == True:
                print("El usuario ha cambiado a: ", usuario_seleccionado)
            else:
                print("Este usuario no se encuentra activo, gilipollas")

    if usuario_encontrado == False:
        print("Usuario no encontrado")
        
    return usuario_seleccionado

#Definicion para añadir un articulo al carrito
def anadir_articulo2(articulos, carrito):
    articulo_encontrado = False         #Esto es importante luego
    print(articulos)
    nombre_articulo = str(input("¿Cual articulo quieres añadir al carrito?: "))
    for objeto in articulos:
        if objeto["nombre"] == nombre_articulo:
            articulo_encontrado = True
            if objeto["activo"] == True:
                carrito.append(objeto)  #Actualiza aqui el carrito con el articulo seleccionado
                print("Artículo añadido: ", objeto)
            else:
                print("Este producto no esta a la venta,gilipollas")
    if articulo_encontrado == False:
        print("Artículo no encontrado")
    return carrito

#Definicion para quitar artículos del carrito(Deberian de poder volver a añadirse si lo solicita el usuario)
def borrararticulo3(carrito):
    if len(carrito) == 0:
        print("El carrito ya está vacio")
    else:
        #Literal copiado de la funcion anterior
        articulo_encontrado = False    
        print(carrito)
        nombre_articulo = str(input("¿Que artículo quiere elminiar?: "))
        for objeto in carrito:
            if objeto["nombre"] == nombre_articulo:
                articulo_encontrado = True
                print("Articulo encontrado: ", objeto)
                carrito.remove(objeto) 
                print("Articulo eliminado correctamente")

        if articulo_encontrado == False:
            print("El articulo no se encuentra en el carrito")
        return carrito
#Definicion para ver carrito y el total de la compra    
def vercarrito4(carrito):
    suma = 0
    contador = 1
    for nombre in carrito:
        nombre_articulo = nombre["nombre"]
        print(contador, ". ", nombre_articulo)
        contador = contador + 1
    for precio in carrito:
        precio_articulo = precio["precio"]
        suma = suma + precio_articulo
    print("El total a pagar es:", suma)
        
#Definicion para teminar la compra
def terminar_compra5(carrito,historialventas,usuario_seleccionado):
    if usuario_seleccionado == None:
        print("Por favor seleccione un usuario")
    print(carrito)
    pythonesmierda = (input("Estas seguro de que quieres terminar la compra?(si/no):")).strip().lower()
    seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
    if seguro == True:
        pythonescaca = carrito
        historialventas.append(usuario_seleccionado)    #PORQUE NO TE ACTUALIZAS AJJAJAJA
        historialventas.append(pythonescaca)     #Lo que deberia de ocurrir aqui  es que se actualize la lista  y luego se vuelque todo pero te lo da todo vacio incluido usuario seleccionado
        carrito.clear()
        print("Compra realizada con éxito")
        print(historialventas)
        return carrito, historialventas
        
#Función historial de ventas
def historial_ventas6(historialventas):
    contador = 1
    for venta in historialventas:
        if contador % 2 != 0:
            print(contador, ". ", venta["nombre"])
            contador = contador + 1
        if contador % 2 == 0:
            print("Ha comprado: ", venta)
        

        
#Función (bastante simple) para vaciar el carrito entero
def vaciarcarrito7(carrito):
    print(carrito)
    pythonesmierda = (input("Estas seguro de que quieres vaciar todo el carrito?(si/no):")).strip().lower()
    seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
    if seguro == True:        
        carrito.clear()
        print("El carrito ahora esta vacío")
    
    return carrito