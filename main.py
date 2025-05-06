from estudiantes.registro import cargar_estudiantes, mostrar_tabla_estudiantes

def main():
    estudiantes = cargar_estudiantes('estudiantes.csv')
    mostrar_tabla_estudiantes(estudiantes)

if __name__ == "__main__":
    main()
