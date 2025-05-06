import csv

def cargar_estudiantes(ruta_archivo):
    estudiantes_validos = []

    with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            nombre = fila['nombre'].strip()
            try:
                nota = float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantes_validos.append({'nombre': nombre, 'nota': nota})
                else:
                    print(f"Nota fuera de rango para {nombre}: {nota}")
            except ValueError:
                print(f"Nota inválida para {nombre}: {fila['nota']}")

    return estudiantes_validos


def mostrar_tabla_estudiantes(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    
    print(f"{'Nombre':<20} {'Nota':>5}")
    print("-" * 26)
    for est in estudiantes_ordenados:
        print(f"{est['nombre']:<20} {est['nota']:>5.2f}")
