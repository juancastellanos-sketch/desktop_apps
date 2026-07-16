from tkinter import *

# ventana principal de la desktop app
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title ("Sistemas guaneta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo a la ventana
ventana_principal.config(bg="green")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# agregamos un objeto de tipo frame sobre la ventana
frame_1 = Frame(ventana_principal)
frame_1.config

# bucle principal
ventana_principal.mainloop()