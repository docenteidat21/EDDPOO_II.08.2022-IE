class Empleado:

    # Constructor
    def __init__(self, codigo, nombre, horas, tarifa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__horas = horas
        self.__tarifa = tarifa
    
    # Métodos de acceso get y set
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre
    
    def getHoras(self):
        return self.__horas

    def getTarifa(self):
        return self.__tarifa

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setHoras(self, horas):
        self.__horas = horas
    
    def setTarifa(self, tarifa):
        self.__tarifa = tarifa
    
    # Métodos

    def sueldoBruto(self):
        return self.getHoras() * self.getTarifa()
    
    def descuento(self):
        return 0.11 * self.sueldoBruto()
    
    def sueldoNeto(self):
        return self.sueldoBruto() - self.descuento()


