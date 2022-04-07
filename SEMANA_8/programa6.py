"""
Implementar una clase que represente un 
empleado, que tenga como atributos su nombre
y su sueldo. En el método __init__ cargar los 
atributos por teclado y luego en otro método 
ver sus datos y por último un método que 
imprima un mensaje si debe pagar impuestos 
(si el sueldo supera a 2250).

"""

class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.sueldo = int(input("Ingrese el sueldo: "))

    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("SUELDO: ", self.sueldo)

    def mostrarCondicion(self):
        if self.sueldo > 2225:
            print("PAGA IMPUESTO")
        else:
            print("NO PAGA INPUESTOS")      

empleado1 = Empleado()
empleado1.mostrarDatos()
empleado1.mostrarCondicion()