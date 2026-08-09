#importamos la libreria
from tkinter import *

ventana = Tk() #creamos una clase llamada ventana del tipo Tk

ventana.title("Primera ventana") # Titulo

ventana.geometry("600x400") #tamaño de la ventana

ventana.iconbitmap("cinebenc_icon.ico") # icono (selecciono un archivo .ico)

ventana.config(bg="#FFFDFD") #cambio el color de fondo

#Metodo pack

miFrame = Frame() #creamos el frame, un contenedor para otros widgets
miFrame.pack(fill="both", expand=1) #lo empaquetamos y le decimos que ocupe todo el espacio disponible (ancho y alto)
miFrame.config(bg="black")    #color del fondo
miFrame.config(width="600", height="400")  #cambiar el tamaño    
# height = altura
# width = ancho
miFrame.config(bd=20) #grosor del borde
miFrame.config(relief="groove") #tipo de borde de la interfaz(flat,raised,sunken,groove ridge)
miFrame.config(cursor="mouse") #diseño del punto del mouse (arrow, circle, heart, man, mouse, etc...)


#metodo place: posiciona un widget con coordenadas x,y fijas (relativas al contenedor)
h
nombreprofesor = Label(miFrame, bg="white", text="Profesor: Ignacio Quiroga") #etiqueta con fondo blanco, sin fg porque el texto por defecto (negro) ya contrasta bien
nombreprofesor.place(x=400, y=330) #posicion fija dentro de miFrame, no de toda la ventana

#metodo grid: posiciona widgets en una tabla de filas y columnas

nombrealumno = Label(miFrame, bg="brown", text="Matias Composto") #fg no especificado, pero el texto default (negro) no se pierde sobre marron, a diferencia de lo que pasaba con fondo negro
nombrealumno.grid(row=0, column=0) #fila 0, columna 0
entradadatos = Entry(miFrame, bg="#D31A1A") #campo de texto editable, para que el usuario escriba
entradadatos.grid(row=0, column=1) #misma fila, columna siguiente, para quedar al lado del label


ventana.mainloop() #siempre al ultimo, mainloop es el que mantiene visible la ventana


#bg = background = color de fondo (lo que está atrás)
#fg = foreground = color de texto/letras (lo que está adelante)