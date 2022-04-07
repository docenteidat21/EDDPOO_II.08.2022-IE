class Persona:

    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Ingrese el sexo: ")
        self.profesion = input("Ingrese la profesión: ")

    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("APELLIDO: ", self.apellido)
        print("EDAD: ", self.edad)
        print("SEXO: ", self.sexo)
        print("PROFESIÓN: ", self.profesion)
        print("")

persona1 = Persona()
persona1.mostrarDatos()

persona2 = Persona()
persona2.mostrarDatos()

