#piedra, papel o tijera
print("Bienvenido al juego de Piedra, Papel o Tijera")

while True:
    opción_usuario1 = input("Jugador 1, elige piedra, papel o tijera: ")
    opción_usuario1 = opción_usuario1.lower()
    while opción_usuario1 != "piedra" and opción_usuario1 != "papel" and opción_usuario1 != "tijera":
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        opción_usuario1 = input("Jugador 1, elige piedra, papel o tijera: ")

    opción_usuario2 = input("Jugador 2, elige piedra, papel o tijera: ")
    opción_usuario2 = opción_usuario2.lower()
    while opción_usuario2 != "piedra" and opción_usuario2 != "papel" and opción_usuario2 != "tijera":
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        opción_usuario2 = input("Jugador 2, elige piedra, papel o tijera: ")

    if opción_usuario1 == opción_usuario2:
        print("¡Empate!")
        print("Ambos jugadores eligieron", opción_usuario1)

    elif opción_usuario1 == "piedra" and opción_usuario2 == "tijera":
        print("¡Jugador 1 gana! Piedra vence a tijera.")

    elif opción_usuario1 == "piedra" and opción_usuario2 == "papel":
        print("¡Jugador 2 gana! Papel vence a piedra.")

    elif opción_usuario1 == "papel" and opción_usuario2 == "piedra":
        print("¡Jugador 1 gana! Papel vence a piedra.")

    elif opción_usuario1 == "papel" and opción_usuario2 == "tijera":
        print("¡Jugador 2 gana! Tijera vence a papel.")

    elif opción_usuario1 == "tijera" and opción_usuario2 == "papel":
        print("¡Jugador 1 gana! Tijera vence a papel.")

    elif opción_usuario1 == "tijera" and opción_usuario2 == "piedra":
        print("¡Jugador 2 gana! Piedra vence a tijera.")
        
    jugar_de_nuevo = input("¿Querés jugar otra vez? (s/n): ")
    if jugar_de_nuevo != "s":
        break    




