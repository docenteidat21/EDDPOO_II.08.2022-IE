"""
Implemente la clase Animal, que tenga como atributos 
nombre, numero_patas y tamaño. En el método __init__ 
cargar los atributos por teclado y en otro método mostrar 
sus datos. Luego  implemente la clase Perro y la clase 
Gato que hereden de la clase Animal. Finalmente cree un 
objeto de las clases hijas uno para cada clase.
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

# LA CLASE PERRO Y LA CLASE GATO SON CLASES HIJAS O SUBCLASE

class Perro(Animal):
    pass

class Gato(Animal):
    pass

# CREANDO OBJETOS DE LA CLASE PERRO

perro1 = Perro()
perro1.mostrarDatos()

# CREANDO OBJETOS DE LA CLASE GATO

gato1 = Gato()
gato1.mostrarDatos()