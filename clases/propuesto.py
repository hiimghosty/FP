"""
Carga un numero binario bit a bit (la cantidad de bits debe ser
multiplo de 3) y cuenta cuantos unos aparecen en cada grupo de 3 bits.
"""

TAMANIO_GRUPO = 3


def pedir_cantidad_bits():
    """Pide la cantidad de bits a cargar; debe ser multiplo de 3 y mayor a 0."""
    cantidad_bits = -1
    while cantidad_bits <= 0 or cantidad_bits % TAMANIO_GRUPO != 0:
        cantidad_bits = int(input("Ingresar un numero multiplo de 3: "))
    return cantidad_bits


def cargar_lista_binaria(cantidad_bits):
    """Pide cada bit (0 o 1) al usuario y los devuelve en una lista."""
    lista_binaria = []
    for numero_bit in range(cantidad_bits):
        bit = int(input(f"Introducir el bit {numero_bit + 1} (0 o 1): "))
        lista_binaria.append(bit)
    return lista_binaria


def contar_unos_por_grupo(lista_binaria, tamanio_grupo=TAMANIO_GRUPO):
    """Devuelve, por cada grupo de 'tamanio_grupo' bits, cuantos son 1."""
    contadores = []
    for inicio in range(0, len(lista_binaria), tamanio_grupo):
        grupo = lista_binaria[inicio:inicio + tamanio_grupo]
        contadores.append(grupo.count(1))
    return contadores


cantidad_bits = pedir_cantidad_bits()
lista_binaria = cargar_lista_binaria(cantidad_bits)
print(lista_binaria)

contadores_de_unos = contar_unos_por_grupo(lista_binaria)
print(contadores_de_unos)
