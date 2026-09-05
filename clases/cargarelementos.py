"""
Carga las notas de un curso y cuenta cuantos alumnos quedaron
por debajo del promedio general.
"""


def pedir_cantidad_alumnos():
    """Pide la cantidad de alumnos del curso (debe ser mayor a 0)."""
    cantidad_alumnos = 0
    while cantidad_alumnos <= 0:
        cantidad_alumnos = int(input("Ingresar la cantidad de alumnos: "))
    return cantidad_alumnos


def cargar_notas(cantidad_alumnos):
    """Pide una nota por cada alumno y las devuelve en una lista."""
    notas = []
    for numero_alumno in range(cantidad_alumnos):
        nota = float(input(f"Ingresar la nota del alumno {numero_alumno + 1}: "))
        notas.append(nota)
    return notas


def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas."""
    return sum(notas) / len(notas)


def contar_inferiores_al_promedio(notas, promedio):
    """Cuenta cuantas notas quedaron por debajo del promedio dado."""
    cantidad_inferiores = 0
    for nota in notas:
        if nota < promedio:
            cantidad_inferiores += 1
    return cantidad_inferiores


cantidad_alumnos = pedir_cantidad_alumnos()
notas = cargar_notas(cantidad_alumnos)
promedio = calcular_promedio(notas)
cantidad_inferiores_al_promedio = contar_inferiores_al_promedio(notas, promedio)

print("Promedio del curso:", promedio)
print("Alumnos por debajo del promedio:", cantidad_inferiores_al_promedio)
