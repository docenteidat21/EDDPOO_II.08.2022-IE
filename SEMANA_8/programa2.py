class Auto:

    def inicializar(self, color, modelo, puertas, llantas, velocidades):
        self.color = color
        self.modelo = modelo
        self.puertas = puertas
        self.llantas = llantas
        self.velocidades = velocidades
    
    def mostrarDatos(self):
        print("COLOR\t\t: ", self.color)
        print("MODELO\t\t: ", self.modelo)
        print("PUERTAS\t\t: ", self.puertas)
        print("LLANTAS\t\t: ", self.llantas)
        print("VELOCIDADES\t: ", self.velocidades)
        print("")

auto1 = Auto()
auto1.inicializar("Rojo", "Yaris", 4, 4, 5)
auto1.mostrarDatos()

auto2 = Auto()
auto2.inicializar("Blanco", "Kia", 4, 4, 5)
auto2.mostrarDatos()

auto3 = Auto()
auto3.inicializar("Azul", "Corola", 4, 4, 5)
auto3.mostrarDatos()