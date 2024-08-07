def metros_a_kilometros(metros):
    return metros / 1000


def kilometros_a_metros(kilometros):
    return kilometros * 1000


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("Bienvenido al Convertidor de Unidades")
    while True:
        print("\n1. Metros a Kilómetros")
        print("2. Kilómetros a Metros")
        print("3. Celsius a Fahrenheit")
        print("4. Fahrenheit a Celsius")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            resultado = metros_a_kilometros(valor)
            print(f"{valor} metros son {resultado} kilómetros")
        elif opcion == "2":
            resultado = kilometros_a_metros(valor)
            print(f"{valor} kilómetros son {resultado} metros")
        elif opcion == "3":
            resultado = celsius_a_fahrenheit(valor)
            print(f"{valor}°C son {resultado}°F")
        elif opcion == "4":
            resultado = fahrenheit_a_celsius(valor)
            print(f"{valor}°F son {resultado}°C")
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
