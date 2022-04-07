from email import message
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Mi calculadora")
ventana.geometry("382x215")
ventana.configure(background = "yellow")

resultado = StringVar()

def suma():
    try:
        suma = int(texto1.get()) + int(texto2.get())
        texto1.delete(0, END)
        texto2.delete(0, END)
        texto1.focus()
        return resultado.set(suma)
    except:
        texto1.delete(0, END)
        texto2.delete(0, END)
        messagebox.showinfo(title = "SUMA", message = "Los datos ingresados son incorrectos...!!!")
        texto1.focus()

def resta():
    resta = int(texto1.get()) - int(texto2.get())
    return resultado.set(resta)

def multiplicacion():
    multiplicacion = int(texto1.get()) * int(texto2.get())
    return resultado.set(multiplicacion)

def division():   
    try:
        division = int(texto1.get()) / int(texto2.get())
        texto1.delete(0, END)
        texto2.delete(0, END)
        texto1.focus()
        return resultado.set(division)
    except ValueError:
        texto1.delete(0, END)
        texto2.delete(0, END)
        messagebox.showinfo(title = "DIVISIÓN", message = "Los datos ingresados son incorrectos...!!!")
        texto1.focus()
    except ZeroDivisionError:
        texto1.delete(0, END)
        texto2.delete(0, END)
        messagebox.showinfo(title = "DIVISIÓN", message = "La división entre 0 no está permitida...!!!")
        texto1.focus()


# CREACIÓN DE ETIQUETAS

etiqueta1 = Label(ventana, text = "Primer número", bg = "yellow", font = ("Arial Bold", 15))
etiqueta1.grid(row = 1, column = 1)

etiqueta2 = Label(ventana, text = "Segundo número", bg = "yellow", font = ("Arial Bold", 15))
etiqueta2.grid(row = 2, column = 1)

etiqueta3 = Label(ventana, bg = "white", font = ("Arial bold", 15), width = 33, textvariable = resultado)
etiqueta3.grid(row = 6, column = 1, columnspan = 2)

# CREACIÓN DE CAJAS DE TEXTO

texto1 = Entry(ventana, font = ("Arial bold", 15))
texto1.grid(row = 1, column = 2)

texto2 = Entry(ventana, font = ("Arial bold", 15))
texto2.grid(row = 2, column = 2)

# CREACIÓN DE BOTONES

boton_suma = Button(ventana, text = "+", bg = "green", fg =  "white", font = ("Arial Bold", 15), width = 10, command = suma)
boton_suma.grid(row = 3, column = 1)

boton_resta = Button(ventana, text = "-", bg = "green", fg =  "white", font = ("Arial Bold", 15), width = 10)
boton_resta.grid(row = 3, column = 2)

boton_multiplicar = Button(ventana, text = "*", bg = "green", fg =  "white", font = ("Arial Bold", 15), width = 10)
boton_multiplicar.grid(row = 4, column = 1)

boton_division = Button(ventana, text = "/", bg = "green", fg =  "white", font = ("Arial Bold", 15), width = 10)
boton_division.grid(row = 4, column = 2)

boton_cerrar = Button(ventana, text = "Cerrar", bg = "gray", fg = "white", font = ("Arial Bold", 15), width = 30)
boton_cerrar.grid(row = 5, column = 1, columnspan = 2)

ventana.mainloop()
