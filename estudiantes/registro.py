import csv


def cargar_estudiantes(nombre_archivo):
    estudiantes = []
    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        for fila in lector:
            if len(fila) != 2:
                continue
            nombre, nota_str = fila
            try:
                nota = float(nota_str)
                if 0.0 <= nota <= 5.0:
                    estudiantes.append((nombre.strip(), nota))
            except ValueError:
                continue
    return estudiantes


def mostrar_tabla(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[0])
    print(f"{'Nombre':<20} | {'Nota'}")
    print("-" * 30)
    for nombre, nota in estudiantes_ordenados:
        print(f"{nombre:<20} | {nota}")


def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0.0
    total = sum(nota for _, nota in estudiantes)
    return total / len(estudiantes)

