from cgitb import text
from tkinter import *

# FUNCIONES
def click():
    etiqueta.configure(text="Hiciste click aquí...!!!")

#FORMULARIO
ventana = Tk()
ventana.title("Mi ventana")
ventana.geometry("750x200")
etiqueta = Label(ventana, text="Hola", font=("Arial Bold", 20))
etiqueta.grid(row=0, column=0)
boton = Button(ventana, text="Click aquí", bg="orange", fg="red", command=click)
boton.grid(row=0, column=1)
texto = Entry(ventana, width=10)
texto.grid(row=0, column=2)

ventana.mainloop()
