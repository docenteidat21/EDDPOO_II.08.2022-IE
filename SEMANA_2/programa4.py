def divide():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("El cociente de los números es: " + str(num1 / num2))
    except ValueError:
        print("El valor ingresado es incorrecto...!!!")
    except ZeroDivisionError:
        print("No se puede dividir entre 0...!!!")
    finally:
        print("Calculo finalizado...!!!")

divide()

        