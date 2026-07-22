tomate = 25
lechuga = 8



while True:
    
    print("¡Bienvenido!")           
    print("Tenemos", tomate, "tomates y", lechuga, "lechugas disponibles.")

    quiere_tomate = input("¿Vas a querer comprar tomate? (si/no): ")
    quiere_lechuga = input("Vas a querer comprar lechuga? (si/no): ")
    
    if quiere_tomate == "si":
        cantidad_tomate = int(input("Cuanto vas a comprar de tomate?: "))
        tomate = tomate - cantidad_tomate
        print("Me dejaste con:", tomate, "de tomates.")

    elif quiere_tomate == "no":
        print("No se compró tomate.")
        break
    if quiere_lechuga == "si":
        cantidad_lechuga = int(input("Cuanto vas a comprar de lechuga?: "))
        lechuga = lechuga - cantidad_lechuga
        print("Me dejaste con:", lechuga, "de lechugas.")

    elif quiere_lechuga == "no":
        print("No se compró lechuga.")
        break



######################################################################################################


print(" ###El profe de programación va a la verdulería### ")
respuesta_tomate = input("¿Tiene tomate? (si/no): ")

if respuesta_tomate == "si":
    print("El profe pidió 1/2 kg de tomate.")

respuesta_lechuga = input("¿Tiene lechuga? (si/no): ")

if respuesta_lechuga == "si":
    print("El profe pidió 1 planta de lechuga.")

print("### El profe terminó comprando: ###")

if respuesta_tomate == "si":
    print("- 1/2 kg de tomate")

if respuesta_lechuga == "si":
    print("- 1 planta de lechuga")

if respuesta_tomate == "si" and respuesta_lechuga == "si":
    
    print("Con lo que compró el profe se hizo una ensalada.")

