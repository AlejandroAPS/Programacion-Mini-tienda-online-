#Definicion del menu gestion de usuarios
def menu_usuarios():          
    print("1.Crear usuario")
    print("2.Listar usuarios")
    print("3.Buscar usuarios por ID")
    print("4.Actualizar usuario")
    print("5.Eliminar ususario")
    print("6.Menú gestión de artículos")
    print("7.Carrito de la compra")
    print("8.Salir del programa")
#Definicion para crear un articulo nuevo {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True}
def crear1(usuarios):
    nuevousuario = {}
    nuevonombre = str(input("Dime el nombre del usuario a añadir:"))
    nuevousuario.update({"ID": len(usuarios) + 1, "nombre": nuevonombre})
    nuevoemail = str(input("Cual es su E-mail?:"))
    nuevousuario.update({"email": nuevoemail })
    pythonestamalhecho = input("Se encuentra en actividad?(si/no):").strip().lower()    #Esta parafernalia es porque al hacer bool(input()) si esta lleno da true y si esta vacio da false por lo que siempre daba true porque python es mierda
    nuevoactividad = pythonestamalhecho in ["si", "sì", "s", "true", "1"]   #(Me ayudo chatGPT) es para comparar el input del tonto usuario a las opciones de esta lista y asi de true o flase bien porque antes solo devolvia true
    nuevousuario.update({"activo": nuevoactividad })
    usuarios.append(nuevousuario)
    return usuarios
#Definicion para mostrar todos los articulos ingresados por el usuario
def mostrar2(usuarios):
    print(usuarios)
#Definicion para buscar por ID de articulo
def buscar3(busqueda, usuarios):
    if busqueda < len(usuarios) + 1:
        for usuario in usuarios:
            if usuario ["ID"] == busqueda:
                print(usuario)
    else:
        print("Usuario no encontrado")
#Definicion para actualizar los usuarios(diccionarios) en la lista de usuarios
def actualizar4(usuarios):
    usuario_encontrado = False    #Esto es importante luego
    nombre_usuario = str(input("¿Cual es el nombre del usuario a actualizar?: "))
    for usuario in usuarios:
        if usuario["nombre"] == nombre_usuario:
            usuario_encontrado = True
            usuario_actualizado = usuario
            print("Usuario encontrado: ", usuario)
            print("Campos disponibles para actualizar:")
            print(list(usuario.keys()))
            clave = str(input("Que campo deseas actualizar?")).strip().lower()
            match clave:
                case "nombre":
                    Nnombre = str(input("Dime que nuevo nombre va a tener:"))
                    usuario["nombre"] = Nnombre 
                case "precio":
                    Nemail = str(input("Dime cual es el nuevo email a usar:"))
                    usuario["email"] = Nemail
                case "activo":
                    pythonesmierda = (input("¿Se encuentra en actividad?(si/no):")).strip().lower()
                    Nactivo = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
                    usuario["activo"] = Nactivo
                case _:
                    print("Opción de campo erronea")
    if usuario_encontrado == False:    #Evita posibles comportamientos extraños/bugs etc (Si lo tocas te toco)
        print("Usuario no encontrado")
    return usuario_actualizado, usuarios
    
def borralacuenta5(usuarios):       #Literal copiado de la funcion anterior
    usuario_encontrado = False    
    nombre_usuario = str(input("¿Cual es el nombre del usuario a borrar?: "))
    for objeto in usuarios:
        if objeto["nombre"] == nombre_usuario:
            usuario_encontrado = True
            print("Usuario encontrado: ", objeto)
            pythonesmierda = (input("Estas seguro de que quieres borrar el usuario(Acción irreversible)(si/no):")).strip().lower()
            seguro = pythonesmierda in ["si", "sì", "s", "true", "1"]  #Es para que le puedas meter el bicho HAY SI DIQUE YO QUIERO QUE ME METAN EL BICHO(lo explico arriba)
            if seguro == True:
               usuarios.remove(objeto) 
               print("Usuario eliminado correctamente")

    if usuario_encontrado == False:
        print("Usuario no encontrado")
    return usuarios