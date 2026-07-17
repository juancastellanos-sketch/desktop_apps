import tkinter as tk

# Dimensiones
ANCHO = 962
ALTO = 600

# Crear ventana
ventana = tk.Tk()
ventana.title("Bandera de Noruega")
ventana.resizable(False, False)

# Crear lienzo
canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO)
canvas.pack()

# Colores oficiales aproximados
ROJO = "#BA0C2F"
BLANCO = "#FFFFFF"
AZUL = "#00205B"

# Fondo rojo
canvas.create_rectangle(0, 0, ANCHO, ALTO, fill=ROJO, outline=ROJO)

# Proporciones
u = ALTO / 16

# Centro de la cruz
x = 6 * u
y = 6 * u

# Anchos
blanco = 2 * u
azul = 1 * u

# Cruz blanca vertical
canvas.create_rectangle(
    x - blanco/2, 0,
    x + blanco/2, ALTO,
    fill=BLANCO,
    outline=BLANCO
)

# Cruz blanca horizontal
canvas.create_rectangle(
    0, y - blanco/2,
    ANCHO, y + blanco/2,
    fill=BLANCO,
    outline=BLANCO
)

# Cruz azul vertical
canvas.create_rectangle(
    x - azul/2, 0,
    x + azul/2, ALTO,
    fill=AZUL,
    outline=AZUL
)

# Cruz azul horizontal
canvas.create_rectangle(
    0, y - azul/2,
    ANCHO, y + azul/2,
    fill=AZUL,
    outline=AZUL
)

ventana.mainloop()