def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir entre cero"


def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Ingresa tu elección (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar números.")
            return

        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida")


# Ejecutar la calculadora
calculadora()
