"""
Genera un vector de numeros aleatorios y calcula su magnitud
(norma euclidiana): raiz cuadrada de la suma de cada componente
al cuadrado.

El original tenia dos errores: pisaba la lista 'A' con un unico
numero random (A = random.randint(...)) en vez de agregarle
elementos, y la funcion 'magnitud' nunca devolvia ni usaba el
resultado calculado.
"""

import random
import math

CANTIDAD_ELEMENTOS = 3
VALOR_MINIMO = 0
VALOR_MAXIMO = 10


def generar_vector_aleatorio(cantidad_elementos, valor_minimo, valor_maximo):
    """Devuelve una lista con numeros aleatorios entre valor_minimo y valor_maximo."""
    return [random.randint(valor_minimo, valor_maximo) for _ in range(cantidad_elementos)]


def calcular_magnitud(vector):
    """Calcula la magnitud (norma euclidiana) de un vector."""
    suma_de_cuadrados = 0
    for componente in vector:
        suma_de_cuadrados += componente ** 2
    return math.sqrt(suma_de_cuadrados)


vector = generar_vector_aleatorio(CANTIDAD_ELEMENTOS, VALOR_MINIMO, VALOR_MAXIMO)
print("Vector generado:", vector)
print("La magnitud del vector es:", calcular_magnitud(vector))
