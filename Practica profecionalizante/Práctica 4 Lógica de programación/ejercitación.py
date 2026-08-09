#Ejercicio 1
print()
print("Bienvenido a la Aventura 'La serpiente veloz'")
#Python World

edad = int(input("Ingrese su edad: "))
altura = int(input("Ingrese su altura en cm: "))

if edad >= 12 and altura >= 150:
    print("¡Bienvenido a la aventura!")
elif edad > 12 and altura < 150:
    print("Lo siento, te falta estatura para esta atracción")
else:
    print("Aún eres muy pequeño para este desafío")


#Ejercicio 2
print()
print("Calculadora de Descuentos 'Eco-Tech'")

#Calculadora de Descuentos "Eco-Tech"

precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_comprada = int(input("Ingrese la cantidad comprada: "))
total_bruto = precio_producto * cantidad_comprada

if cantidad_comprada >= 10:
    descuento = total_bruto * 0.20
    total_neto = total_bruto - descuento
    print("Total a pagar con descuento del 20%:", total_neto)
elif cantidad_comprada >= 5 and cantidad_comprada <= 9:
    descuento = total_bruto * 0.10
    total_neto = total_bruto - descuento
    print("Total a pagar con descuento del 10%:", total_neto)
else:
    print("No hay descuento aplicable")


#Ejercicio 3

print()
print("Bienvenido al Oráculo de los Elementos")

#Oráculo de los Elementos

numero_elegido = int(input("Ingrese un número del 1 al 100 para conocer su elemento asociado: "))

if numero_elegido % 2 == 0 and numero_elegido > 50:
    print("Perteneces al clan del FUEGO")
elif numero_elegido % 2 == 0 and numero_elegido <= 50:
    print("Perteneces al clan del AGUA")
elif numero_elegido % 2 != 0:
    print("Perteneces al clan del AIRE")
else:
    print("Perteneces al clan de la TIERRA")