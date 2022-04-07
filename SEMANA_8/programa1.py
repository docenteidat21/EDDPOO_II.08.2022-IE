class Auto:

    # Atributos
    color = ""
    modelo = ""
    puertas = 0
    llantas = 0
    velocidades = 0

    # Métodos
    def mostrarDatos(self):
        print("COLOR: ", self.color)
        print("MODELO: ", self.modelo)
        print("PUERTAS: ", self.puertas)
        print("LLANTAS: ", self.llantas)
        print("VELOCIDADES: ", self.velocidades)

# Creando el 1er objeto
auto1 = Auto()
auto1.color = "Azul"
auto1.modelo = "Yaris"
auto1.puertas = 4
auto1.llantas = 4
auto1.velocidades = 5
auto1.mostrarDatos()
print("")

# Creando el 2do objeto
auto2 = Auto()
auto2.color = "Negro"
auto2.modelo = "Corola"
auto2.puertas = 5
auto2.llantas = 4
auto2.velocidades = 5
auto2.mostrarDatos()
print("")

# Creando el 3er objeto
auto3 = Auto()
auto3.color = "Rojo"
auto3.modelo = "Kia"
auto3.puertas = 5
auto3.llantas = 4
auto3.velocidades = 5
auto3.mostrarDatos()