# para retomar un poco
"""
print(productos)

print("El primer producto es:", productos[0])
print("El último producto es:", productos[4])

print("La cantidad de productos es:", len(productos))

equipos = ["Argentina", "Argelia", "Austria", "Jordania"]

print(equipos[0])
print(equipos[3])
print(len(equipos))

for equipo in equipos:
    print("Jugando:", equipo)

"""

productos = []

while True:
    pertenece = False
    producto = input("Ingrese un producto (o 'salir' para terminar): ").lower()
    if producto in productos:
        respuesta = ""
        print("El producto ya está en la lista.")
        respuesta = input("Desea ingresar el producto igualmente? (s/n): ").lower()
        if respuesta == "n":
            continue
        elif respuesta == "s":
            productos.append(producto)
            continue
        else:
            print("Opción inválida. El producto no se agregará.")
            continue

    if producto == "salir":
            break
    productos.append(producto)


print("Los productos ingresados son:")
for producto in productos:
    print("-", producto)



"""

#para revisar un valor en una lista

valores = [10, 20, 30, 40, 50]
valor = 30
if valor in valores:
    print("El valor", valor, "está en la lista")
else:
    print("El valor", valor, "no está en la lista")

"""