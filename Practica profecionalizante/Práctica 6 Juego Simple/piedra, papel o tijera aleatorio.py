import random
puntaje_usuario1 = 0
puntaje_bot = 0


#piedra, papel o tijera
print("Bienvenido al juego de Piedra, Papel o Tijera")

while True:
    bot =random.randint(1, 3)
    if bot == 1:
        bot = "piedra"
    elif bot == 2:
        bot = "papel"
    elif bot == 3:
        bot = "tijera"
    opción_usuario1 = input("Jugador 1, elige piedra, papel o tijera: ")
    opción_usuario1 = opción_usuario1.lower()
    while opción_usuario1 != "piedra" and opción_usuario1 != "papel" and opción_usuario1 != "tijera":
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        opción_usuario1 = input("Jugador 1, elige piedra, papel o tijera: ")



    if opción_usuario1 == bot:
        print("¡Empate!")
        print("Ambos jugadores eligieron", opción_usuario1)
        print("PUNTAJES")
        print("Jugador:", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "piedra" and bot == "tijera":
        print("¡Jugador gana! Piedra vence a tijera.")
        puntaje_usuario1 += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "piedra" and bot == "papel":
        print("¡Bot gana! Papel vence a piedra.")
        puntaje_bot += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "papel" and bot == "piedra":
        print("¡Jugador gana! Papel vence a piedra.")
        puntaje_usuario1 += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "papel" and bot == "tijera":
        print("¡Bot gana! Tijera vence a papel.")
        puntaje_bot += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "tijera" and bot == "papel":
        print("¡Jugador gana! Tijera vence a papel.")
        puntaje_usuario1 += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)

    elif opción_usuario1 == "tijera" and bot == "piedra":
        print("¡Bot gana! Piedra vence a tijera.")
        puntaje_bot += 1
        print("PUNTAJES")
        print("Jugador: ", puntaje_usuario1)
        print("Bot:", puntaje_bot)


    jugar_de_nuevo = input("¿Querés jugar otra vez? (s/n): ")
    if jugar_de_nuevo != "s":
        if puntaje_usuario1 > puntaje_bot:
            print("¡Te felicito! Sos mas inteligente (creo) que una maquina, le ganaste con un puntaje de", puntaje_usuario1, "a", puntaje_bot)
        elif puntaje_usuario1 < puntaje_bot:
            print("¡Perdiste contra una maquina, jajjaja! Con un puntaje de", puntaje_usuario1, "a", puntaje_bot)
        else:
            print("¡Empate! Con un puntaje de", puntaje_usuario1, "a", puntaje_bot)
        break    





