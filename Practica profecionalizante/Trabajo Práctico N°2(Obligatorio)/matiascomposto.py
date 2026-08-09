usuarios = []

while True:

    print ("                MENU")
    print("")
    print("············································")
    print("")
    print("SELECCIONE UNA OPCION")
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    print("3. Salir")
    print("")
    print("············································")
    print("")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        print("")
        print("············································")
        usuarios.append(input("Ingrese el nombre de usuario: "))
        print("")
        print("Usuario registrado correctamente.")
        print("")


    elif opcion == "2":
        print("")
        print("············································")
        print("")
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("")
            print("Bienvenido,", nombre_usuario)
            print("")
            while True:
                sale = input("Ingrese 'salir' para cerrar sesión: ")
                if sale.lower() == "salir":
                    print("")
                    print("Sesión cerrada.")
                    print("")
                    break

        else:
            print("············································")
            print("")
            print("Usuario incorrecto.")
            print("")


    elif opcion == "3":
        print("")
        print("············································")
        print("Saliendo del programa...")
        break

    else:
        print("")
        print("Opción inválida. Por favor, seleccione una opción válida.")
        print("")
