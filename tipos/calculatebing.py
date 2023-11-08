"""
Este módulo contiene una calculadora simple que puede realizar operaciones básicas
como suma, resta, multiplicación y división.
"""


def suma(a, b):
    """
    Esta función toma dos números, a y b, y devuelve su suma.
    """
    return a + b


def resta(a, b):
    """
    Esta función toma dos números, a y b, y devuelve su resta.
    """
    return a - b


def multiplicacion(a, b):
    """
    Esta función toma dos números, a y b, y devuelve su multiplicación.
    """
    return a * b


def division(a, b):
    """
    Esta función toma dos números, a y b, y devuelve su división si b no es cero.
    Si b es cero, devuelve un mensaje de error.
    """
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def input_numero(mensaje):
    """
    Esta función solicita al usuario que introduzca un número.
    Si el usuario introduce algo que no es un número, se muestra un mensaje de error
    y se vuelve a solicitar la entrada.
    Este proceso se repite hasta que el usuario introduce un número válido.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número.")


def input_opcion(mensaje):
    """
    Esta función solicita al usuario que introduzca un número entero entre 1 y 5.
    Si el usuario introduce algo que no es un número entero, o un número
    que no está entre 1 y 5, se muestra un mensaje de error y se vuelve a solicitar la entrada.
    Este proceso se repite hasta que el usuario introduce un número válido.
    """
    while True:
        try:
            opcion_menu = int(input(mensaje))
            if opcion_menu >= 1 and opcion_menu <= 5:
                return opcion_menu
            else:
                print("Por favor, introduce un número entre 1 y 5.")
        except ValueError:
            print("Por favor, introduce un número entero.")


while True:
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicación")
    print("4: División")
    print("5: Salir")

    opcion = input_opcion("Elige una opción: ")

    if opcion == 5:
        break

    num1 = input_numero("Ingresa el primer número: ")
    num2 = input_numero("Ingresa el segundo número: ")

    if opcion == 1:
        print("Resultado: ", suma(num1, num2))
    elif opcion == 2:
        print("Resultado: ", resta(num1, num2))
    elif opcion == 3:
        print("Resultado: ", multiplicacion(num1, num2))
    elif opcion == 4:
        print("Resultado: ", division(num1, num2))
