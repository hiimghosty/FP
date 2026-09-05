"""
Calcula la magnitud (norma euclidiana) de un vector:
raiz cuadrada de la suma de cada componente al cuadrado.
"""

import math


def calcular_magnitud(vector):
    """Calcula la magnitud (norma euclidiana) de un vector."""
    suma_de_cuadrados = 0
    for componente in vector:
        suma_de_cuadrados += componente ** 2
    return math.sqrt(suma_de_cuadrados)


vector = [20, 30, 40]
print("La magnitud del vector es:", calcular_magnitud(vector))
