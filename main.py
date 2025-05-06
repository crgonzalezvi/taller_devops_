from estudiantes.registro import cargar_estudiantes

def main():
    estudiantes = cargar_estudiantes('estudiantes.csv')
    print(estudiantes)

if __name__ == "__main__":
    main()
