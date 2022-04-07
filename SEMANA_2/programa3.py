try:
    a = 5
    b = 0
    print(a / b)

except TypeError:
    print("Operación no soportada...!!!")

except ZeroDivisionError:
    print("División por cero no permitida...!!!")