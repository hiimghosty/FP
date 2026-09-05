"""
Genera un numero binario aleatorio y, cada 3 bits, inserta cuantos
unos aparecieron en ese grupo de 3.

Ejemplo: 110 010 111  ->  1 1 0 2 0 1 0 1 1 1 1 3
"""

import random

TAMANIO_GRUPO = 3


def pedir_cantidad_bits():
    """Pide al usuario una cantidad de bits multiplo de 3 y la devuelve."""
    cantidad_bits = -1
    while cantidad_bits % TAMANIO_GRUPO != 0 or cantidad_bits <= 0:
        cantidad_bits = int(input("Ingresar la cantidad de bits (multiplo de 3): "))
    return cantidad_bits


def generar_numero_binario(cantidad_bits):
    """Devuelve una lista de 0s y 1s generados al azar."""
    return [random.randint(0, 1) for _ in range(cantidad_bits)]


def contar_unos_por_grupo(numero_binario, tamanio_grupo=TAMANIO_GRUPO):
    """Devuelve, por cada grupo de 'tamanio_grupo' bits, cuantos son 1."""
    contadores = []
    for inicio in range(0, len(numero_binario), tamanio_grupo):
        grupo = numero_binario[inicio:inicio + tamanio_grupo]
        contadores.append(grupo.count(1))
    return contadores


def insertar_contadores(numero_binario, contadores, tamanio_grupo=TAMANIO_GRUPO):
    """Arma la lista final intercalando cada grupo de bits con su contador."""
    resultado = []
    indice_grupo = 0
    for inicio in range(0, len(numero_binario), tamanio_grupo):
        grupo = numero_binario[inicio:inicio + tamanio_grupo]
        for bit in grupo:
            resultado.append(bit)
        resultado.append(contadores[indice_grupo])
        indice_grupo = indice_grupo + 1
    return resultado


cantidad_bits = pedir_cantidad_bits()
numero_binario = generar_numero_binario(cantidad_bits)
contadores_de_unos = contar_unos_por_grupo(numero_binario)
numero_final = insertar_contadores(numero_binario, contadores_de_unos)

print("Numero binario generado:", numero_binario)
print("Unos por grupo de 3:", contadores_de_unos)
print("Numero final con contadores insertados:", numero_final)
