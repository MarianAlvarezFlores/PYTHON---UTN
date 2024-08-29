import tkinter as tk
from tkinter import colorchooser

# Tomo entrada y los muestro

def mostrar_datos ():
    """Esta función permite mostrar los datos ingresados por consola"""
    nombre = entrada_nombre.get ()
    apellido = entrada_apellido.get ()
    edad = entrada_edad.get ()
    print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")


def cambiar_color_fondo ():
    """Esta función permite elegir el color de fondo de la app"""
    color = colorchooser.askcolor()[1]  # color en formato hexadecimal
    if color:  
        root.config(bg=color)

# Ventana principal

root = tk.Tk ()
root.title ("App de Alta de Datos y Cambio de Fondo")
root.geometry ("400x300")

# Entrada

tk.Label (root, text="Nombre:").pack(pady=5)
entrada_nombre = tk.Entry (root)
entrada_nombre.pack ()

tk.Label (root, text="Apellido:").pack(pady=5)
entrada_apellido = tk.Entry (root)
entrada_apellido.pack ()

tk.Label (root, text="Edad:").pack (pady=5)
entrada_edad = tk.Entry (root)
entrada_edad.pack ()

# Botón para alta de datos

boton_mostrar = tk.Button (root, text="Mostrar Datos", command=mostrar_datos)
boton_mostrar.pack (pady=20)

# Botón para cambiar el color de fondo

boton_color = tk.Button (root, text="Cambiar Color de Fondo", command=cambiar_color_fondo)
boton_color.pack (pady=10)

root.mainloop ()