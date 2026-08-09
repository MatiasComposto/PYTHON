while True:
    opcion = input(" Ingrese una opción (1: Tabla de multiplicar, 2: Contador hacia atrás, 3: Salir): ")

    if opcion == "1":
        numero = int(input("Ingrese un número del 1 al 10 para ver su tabla de multiplicar: "))

        contador = 1
        while contador <= 10:
            print(numero, "x", contador, "=", numero * contador)
            contador += 1

        numero1 = int(input("Ingrese un número del 1 al 10 para ver su tabla de multiplicar: "))

        contador = 10
        while contador <= 10 and contador > 0:
            print(numero1, "x", contador, "=", numero1 * contador)
            contador -= 1

    elif opcion == "2":
        contador = 10
        while contador >= 1:
            print(contador, end=",")
            contador -= 1
        print()

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")