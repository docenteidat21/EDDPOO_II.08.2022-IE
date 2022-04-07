"""
Realizar un programa que simule tirar dos dados 
y luego muestre los valores que aparecieron. 
Si la suma de dichos números es igual a 9 mostrar 
un mensaje de “Has ganado” sino mostrar “Has perdido”.
"""

from random import randint

dado1 = randint(1, 6)
dado2 = randint(1, 6)
suma = dado1 + dado2

print("DADO 1: ", dado1)
print("DADO 2: ", dado2)
print("SUMA: ", suma)

if suma == 9:
    print("HAS GANADO...!!!")
else:
    print("HAS PERDIDO...!!!")

