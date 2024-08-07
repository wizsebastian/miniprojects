class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea = self.tareas.pop(indice)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Índice de tarea inválido.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i+1}. {tarea}")
        else:
            print("No hay tareas pendientes.")


def main():
    lista = ListaDeTareas()
    while True:
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tarea = input("Ingresa la nueva tarea: ")
            lista.agregar_tarea(tarea)
        elif opcion == "2":
            indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
            lista.eliminar_tarea(indice)
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
