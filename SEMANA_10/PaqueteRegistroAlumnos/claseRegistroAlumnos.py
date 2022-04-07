class RegistroAlumnos:

    # Constructor
    def __init__(self):
        self.__nombre = ""
        self.__apellidoPaterno = ""
        self.__apellidoMaterno = ""
        self.__codigo = ""
    
    # Métodos de acceso get y set
    def getNombre(self):
        return self.__nombre

    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    
    def getApellidoMaterno(self):
        return self.__apellidoMaterno

    def getCodigo(self):
        return self.__codigo

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno
    
    def setApellidoMaterno(self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    