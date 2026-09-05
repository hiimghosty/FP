"""
Genera las temperaturas de febrero (29 dias) al azar y calcula el
promedio de temperatura entre el dia 21 y el dia 27 (ambos incluidos).
"""

import random

CANTIDAD_DIAS_FEBRERO = 29
TEMPERATURA_MINIMA = 15
TEMPERATURA_MAXIMA = 30
DIA_INICIO_RANGO = 21
DIA_FIN_RANGO = 27


def generar_temperaturas_mes(cantidad_dias, temperatura_minima, temperatura_maxima):
    """Devuelve una lista con una temperatura aleatoria por cada dia del mes."""
    return [random.randint(temperatura_minima, temperatura_maxima) for _ in range(cantidad_dias)]


def calcular_promedio_rango(temperaturas, dia_inicio, dia_fin):
    """Promedia las temperaturas entre dia_inicio y dia_fin (1-indexados, ambos incluidos)."""
    temperaturas_del_rango = temperaturas[dia_inicio - 1:dia_fin]
    return sum(temperaturas_del_rango) / len(temperaturas_del_rango)


temperaturas_febrero = generar_temperaturas_mes(
    CANTIDAD_DIAS_FEBRERO, TEMPERATURA_MINIMA, TEMPERATURA_MAXIMA
)
print(temperaturas_febrero)

print(f"Temperaturas entre el dia {DIA_INICIO_RANGO} y el dia {DIA_FIN_RANGO}:")
print(temperaturas_febrero[DIA_INICIO_RANGO - 1:DIA_FIN_RANGO])

promedio_del_rango = calcular_promedio_rango(temperaturas_febrero, DIA_INICIO_RANGO, DIA_FIN_RANGO)
print("Promedio del rango:", promedio_del_rango)
