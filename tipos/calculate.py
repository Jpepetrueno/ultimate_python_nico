"""
Este módulo contiene una calculadora simple que puede realizar operaciones básicas
como suma, resta, multiplicación y división.
"""


# Definición de las funciones para las operaciones de la calculadora
def suma(a, b):
    """Suma dos números."""
    return a + b


def resta(a, b):
    """Resta dos números."""
    return a - b


def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b


def division(a, b):
    """Divide dos números. Si el divisor es cero, devuelve un mensaje de error."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero"


# Función para solicitar al usuario que introduzca un número
def input_numero(mensaje):
    """Solicita al usuario que introduzca un número. Si el usuario introduce algo
    que no es un número, se muestra un mensaje de error y se vuelve a solicitar la entrada.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número.")


# Función para solicitar al usuario que elija una opción del menú
def input_opcion(mensaje, min_value, max_value):
    """Solicita al usuario que introduzca un número entero entre min_value y max_value.
    Si el usuario introduce algo que no es un número entero, o un número que no está
    entre min_value y max_value, se muestra un mensaje de error y se vuelve a solicitar la entrada.
    """
    while True:
        try:
            opcion_menu = int(input(mensaje))
            if min_value <= opcion_menu <= max_value:
                return opcion_menu
            else:
                print(
                    f"Por favor, introduce un número entre {min_value} y {max_value}."
                )
        except ValueError:
            print("Por favor, introduce un número entero.")


# Función principal del programa
def main(): """
    Esta es la función principal del programa. 
    Muestra un menú de operaciones de calculadora al usuario y solicita que elija una opción. 
    Luego, solicita al usuario que introduzca dos números y realiza la operación seleccionada en esos números. 
    Si el usuario elige "Salir", el programa termina.
    """
    # Diccionario que mapea las opciones del menú a las funciones correspondientes
    operaciones = {1: suma, 2: resta, 3: multiplicacion, 4: division}

    while True:
        # Imprimir el menú
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicación")
        print("4: División")
        print("5: Salir")

        # Solicitar al usuario que elija una opción
        opcion = input_opcion("Elige una opción: ", 1, 5)

        # Si el usuario elige "Salir", terminar el programa
        if opcion == 5:
            break

        # Solicitar al usuario que introduzca dos números
        num1 = input_numero("Ingresa el primer número: ")
        num2 = input_numero("Ingresa el segundo número: ")

        # Realizar la operación correspondiente y mostrar el resultado
        operacion = operaciones.get(opcion)
        resultado = operacion(num1, num2)
        print(f"Resultado: {resultado}")


# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
