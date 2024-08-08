def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"


def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        eleccion = input("Introduce tu elección (1/2/3/4): ")

        if eleccion in ["1", "2", "3", "4"]:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if eleccion == "1":
                print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")

            elif eleccion == "2":
                print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")

            elif eleccion == "3":
                print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")

            elif eleccion == "4":
                resultado = division(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")

            # Preguntar si el usuario quiere realizar otra operación
            siguiente_calculo = input("¿Quieres realizar otra operación? (s/n): ")
            if siguiente_calculo.lower() != "s":
                break
        else:
            print("Entrada inválida. Por favor, elige una opción válida.")


if __name__ == "__main__":
    calculadora()
