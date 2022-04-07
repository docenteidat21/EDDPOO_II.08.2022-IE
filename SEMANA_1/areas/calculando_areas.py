from area_cuadrado import cuadrado
from area_rectangulo import rectangulo
from area_trapecio import trapecio

# CUADRADO
lado = int(input("Ingrese el lado del cuadrado: "))
print("AREA CUADRADO: ", cuadrado(lado))

# RECTANGULO
base = int(input("Ingrese la base del rectángulo:"))
altura = int(input("Ingrese la altura del rectángulo:"))
print("AREA RECTANGULO: ", rectangulo(base, altura))

# TRAPECIO
base_mayor = int(input("Ingrese la base mayor del trapecio:"))
base_menor = int(input("Ingrese la base menor del trapecio:"))
altura = int(input("Ingrese la altura del trapecio:"))
print("AREA TRAPECIO: ", trapecio(base_mayor, base_menor, altura))
