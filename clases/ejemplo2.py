"""
Genera las temperaturas de febrero (29 dias) al azar y encuentra
cual fue la mas alta y en que dia ocurrio.
"""

import random

CANTIDAD_DIAS_FEBRERO = 29
TEMPERATURA_MINIMA = 15
TEMPERATURA_MAXIMA = 30


def generar_temperaturas_mes(cantidad_dias, temperatura_minima, temperatura_maxima):
    """Devuelve una lista con una temperatura aleatoria por cada dia del mes."""
    return [random.randint(temperatura_minima, temperatura_maxima) for _ in range(cantidad_dias)]


def obtener_dia_de_mayor_temperatura(temperaturas):
    """Devuelve una tupla (temperatura_maxima, dia) con el dia en formato 1-indexado."""
    temperatura_maxima = max(temperaturas)
    dia = temperaturas.index(temperatura_maxima) + 1
    return temperatura_maxima, dia


temperaturas_febrero = generar_temperaturas_mes(
    CANTIDAD_DIAS_FEBRERO, TEMPERATURA_MINIMA, TEMPERATURA_MAXIMA
)
temperatura_maxima, dia_de_mayor_temperatura = obtener_dia_de_mayor_temperatura(temperaturas_febrero)

print(temperaturas_febrero)
print("La mayor temperatura es:", temperatura_maxima)
print("y ocurre en el dia nro:", dia_de_mayor_temperatura)
