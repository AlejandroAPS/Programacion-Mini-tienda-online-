#Definicion del menu
def menu_articulos():             
    print("1.Crear artículo")
    print("2.Listar artículos")
    print("3.Buscar artículos por id")
    print("4.Actualizar artículo")
    print("5.Eliminar artículo")
    print("6.Menú gestión de usuarios")
    print("7.Carrito de la compra")
    print("8.Salir del programa")
#Definicion para crear un articulo nuevo
def crear1(articulos):
    nuevoarticulo = {}
    nuevonombre = str(input("Dime el nombre del producto a añadir:"))
    nuevoarticulo.update({"ID": len(articulos) + 1, "nombre": nuevonombre})
    nuevoprecio = float(input("Que precio va a tener?:"))
    nuevoarticulo.update({"precio": nuevoprecio })
    nuevostock = int(input("Que tanto stock hay?:"))
    nuevoarticulo.update({"stock": nuevostock })
    pythonestamalhecho = input("Se puede vender ya mismo? (si/no):").strip().lower()    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba false porque python es mierda
    nuevoactividad = pythonestamalhecho in ["si", "sì", "s", "true", "1"]   #(Me ayudo chatGPT) es para comparar el input de usuaior a las opciones de esta lista y  asi de true o flase bien porque antes solo devolvia true
    nuevoarticulo.update({"activo": nuevoactividad })
    articulos.append(nuevoarticulo)
    return articulos, articulos
#Definicion para mostrar todos los articulos ingresados por el usuario
def mostrar2(articulos):
    print(articulos)
#Definicion para buscar por ID de articulo
def buscar3(articulos, busqueda):
    if busqueda < len(articulos) + 1:
        for articulo in articulos:
            if articulo ["ID"] == busqueda:
                print(articulo)
    else:
        print("Artículo no encontrado")
#Definicion para actualizar los articulos(diccionarios) en la lista de articulos
def actualizar4(articulos):
    articulo_encontrado = False    #Esto es importante luego
    nombre_articulo = str(input("¿Cual es el nombre del artículo a actualizar?: "))
    for objeto in articulos:
        if objeto["nombre"] == nombre_articulo:
            articulo_encontrado = True
            objeto_actualizado = objeto
            print("Artículo encontrado: ", objeto)
            print("Campos disponibles para actualizar:")
            print(list(objeto.keys()))  
            clave = str(input("Que campo deseas actualizar?(ID es el único que no se puede actualizar)")).strip().lower()
            match clave:
                case "nombre":
                    Nnombre = str(input("Dime el nuevo nombre que va a tener"))
                    objeto["nombre"] = Nnombre 
                case "precio":
                    Nprecio = float(input("Dime el nuevo precio que va a tener:"))
                    objeto["precio"] = Nprecio
                case "stock":
                    Nstock = int(input("Dime la nueva cantidad de stcok del producto:"))
                    objeto["stock"] = Nstock
                case "activo":
                    pythonesmierda = (input("Dime si esta listo para venta o no(si/no):")).strip().lower()
                    Nactivo = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
                    objeto["activo"] = Nactivo
                case _:
                    print("Opción de campo erronea")
    if articulo_encontrado == False:    #Evita posibles comportamientos extraños/bugs etc (Si lo tocas te toco)
        print("Artículo no encontrado")
    return objeto_actualizado, articulos


def borralacuenta5(articulos):       #Literal  copiado de la funcion anterior
    articulo_encontrado = False    
    nombre_articulo = str(input("¿Cual es el nombre del artículo a borrar de la lista?: "))
    for objeto in articulos:
        if objeto["nombre"] == nombre_articulo:
            articulo_encontrado = True
            print("Artículo encontrado: ", objeto)
            pythonesmierda = (input("Estas seguro de que quieres borrar el artículo(Acción irreversible)(si/no):")).strip().lower()
            seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
            if seguro == True:
               articulos.remove(objeto) 
               print("Artículo eliminado correctamente")

    if articulo_encontrado == False:
        print("Artículo no encontrado")
    return articulos