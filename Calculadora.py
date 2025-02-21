# Funciones para operaciones básicas
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
        return "Error! División por 0."

# Menú de opciones
def calculadora():
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        try:
            operacion = int(input("Selecciona el número de la operación (1/2/3/4): "))

            if operacion in (1, 2, 3, 4):
                numero1 = float(input("Introduce el primer número: "))
                numero2 = float(input("Introduce el segundo número: "))

                if operacion == 1:
                    print(f"Resultado: {suma(numero1, numero2)}")
                elif operacion == 2:
                    print(f"Resultado: {resta(numero1, numero2)}")
                elif operacion == 3:
                    print(f"Resultado: {multiplicacion(numero1, numero2)}")
                elif operacion == 4:
                    print(f"Resultado: {division(numero1, numero2)}")

                siguiente = input("¿Quieres hacer otra operación? (si/no): ").lower()
                if siguiente != 'si':
                    print("¡Hasta luego!")
                    break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números.")

# Llamada a la función de la calculadora
calculadora()
