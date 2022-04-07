def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0...!!!")
        return "Operación errónea...!!!"

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
except ValueError:
    print("Los valores ingresados son incorrectos...!!!")

operacion = input("Ingrese la operación a realizar: ")

if operacion == "SUMA":
    print("LA SUMA ES \t: ", suma(num1, num2))

elif operacion == "RESTA":
    print("LA DIFERENCIA ES \t: ", resta(num1, num2))

elif operacion == "MULTIPLICACION":
    print("EL PRODUCTO ES \t: ", multiplicacion(num1, num2))

elif operacion == "DIVISION":
    print("EL COCIENTE ES \t: ", division(num1, num2))

else:
    print("Operación no contemplada...!!!")

print("Gracias por usar el programa...!!!")

