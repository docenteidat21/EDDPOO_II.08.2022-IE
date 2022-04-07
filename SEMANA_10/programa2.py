"""
Implemente la clase Animal, que tenga como atributos 
nombre, numero_patas y tamaño. En el método __init__ 
cargar los atributos por teclado y en otro método 
mostrar sus datos. Luego  implemente la clase Canino 
que tiene como atributo raza y la clase Perro que tiene 
como atributo numero_vacunas, la clase Canino hereda de la 
clase Animal y la clase Perro hereda de la clase Canino. 
Finalmente cree dos objetos de la clase Perro.
"""

class Animal:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del animal: ")
        self.numero_patas = int(input("Ingrese el número del patas del animal: "))
        self.tamaño = input("Ingrese el tamaño del animal: ")
    
    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("NÚMERO DE PATAS: ", self.numero_patas)
        print("TAMAÑO: ", self.tamaño)

class Canino(Animal):

    def __init__(self):
        super().__init__()
        self.raza = input("Ingrese la raza del canino: ")
    
    def mostrarDatos(self):
        super().mostrarDatos()
        print("RAZA: ", self.raza)

class Perro(Canino):

    def __init__(self):
        super().__init__()
        self.numero_vacunas = int(input("Ingrese la cantidad de vacunas que tiene el perro: "))

    def mostrarDatos(self):
        super().mostrarDatos()
        print("VACUNAS: ", self.numero_vacunas)

# CREANDO OBJETOS DE LA CLASE PERRO

perro1 = Perro()
perro1.mostrarDatos()





