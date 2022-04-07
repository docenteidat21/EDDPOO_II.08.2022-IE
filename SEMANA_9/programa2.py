class Persona:

    # Método Constructor
    def __init__(self):
        self.__codigo = input("Ingrese su código: ")
        self.__nombre = input("Ingrese su nombre: ")
        self.__edad = int(input("Ingrese su edad: "))
    
    # Métodos de acceso get y set
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setEdad(self, edad):
        self.__edad = edad

# Creación de objetos
persona1 = Persona()
print("CÓDIGO: ", persona1.getCodigo())
print("NOMBRE: ", persona1.getNombre())
print("EDAD: ", persona1.getEdad())