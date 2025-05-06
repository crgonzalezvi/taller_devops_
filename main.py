from estudiantes.registro import (
    cargar_estudiantes,
    mostrar_tabla,
    calcular_promedio,
)


def main():
    archivo = "estudiantes.csv"
    estudiantes = cargar_estudiantes(archivo)
    mostrar_tabla(estudiantes)
    promedio = calcular_promedio(estudiantes)
    print(f"\nPromedio general: {promedio:.2f}")


if __name__ == "__main__":
    main()
