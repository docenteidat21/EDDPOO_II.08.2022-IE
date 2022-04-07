"""
Implementar una clase llamada Alumno que 
tenga como atributos su nombre y su nota. 
Definir los métodos para inicializar sus 
atributos, imprimirlos y mostrar un mensaje 
si está APROBADO (nota mayor o igual a 13). 
Definir dos objetos de la clase Alumno.

"""

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrarDatos(self):
        print("NOMBRE: ", self.nombre)
        print("NOTA: ", self.nota)

    def mostrarCondicion(self):
        if self.nota >= 13:
            print("APROBADO...!!!")
        else:
            print("DESAPROBADO...!!!")

# INSTANCIANDO LA CLASE
# CREACIÓN DE OBJETOS

alumno1 = Alumno("Kenny", 20)
alumno1.mostrarDatos()
alumno1.mostrarCondicion()

alumno2 = Alumno("Juan", 10)
alumno2.mostrarDatos()
alumno2.mostrarCondicion()

