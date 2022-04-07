class Alumno:

    # Constructor
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = nota1
        self.__nota2 = nota2
    
    # Métodos de acceso get y set
    def getNombre(self):
        return self.__nombre

    def getNota1(self):
        return self.__nota1
    
    def getNota2(self):
        return self.__nota2
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setNota1(self, nota1):
        self.__nota1 = nota1
    
    def setNota2(self, nota2):
        self.__nota2 = nota2
    
    # Métodos
    def promedio(self):
        return (self.getNota1() + self.getNota2()) / 2

