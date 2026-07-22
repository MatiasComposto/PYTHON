"""

#Entendiendo listas y bucles for
for i in range(4):
    print(i)
equipos = ["Argentina", "Brasil", "Francia", "España"]

for i in range(len(equipos)):
    print(i, "->", equipos[i])



"""
#PROGRAMA MUNDIALITO
import random

print("Bienvenido al Mundialito de Python")
print()
print("////////////////////////////////////////////////")
print()
print("Partidos del mundialito:")


equipos = ["Argentina", "Brasil", "Francia", "España", "Paraguay", "Portugal", "Peru", "Uruguay"]
puntos = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(equipos)):
    for j in range(len(equipos)):
        if i <= j:
            continue
        print("")
        print(equipos[i], "vs", equipos[j])
        goles_i = random.randint(0, 7)
        goles_j = random.randint(0, 7)

        print(equipos[i], goles_i, "-", goles_j, equipos[j])
        if goles_i > goles_j:
            print (equipos[i], "gana el partido")
            puntos[i] += 3



        elif goles_i < goles_j:
            print (equipos[j], "gana el partido")
            puntos[j] += 3


        else:
            print ("Empate")
            puntos[i] += 1
            puntos[j] += 1

for i in range(len(puntos)):
    print("")
    print(equipos [i], puntos[i])







#modo de puntajes





