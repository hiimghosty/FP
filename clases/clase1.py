"""
Demostraciones basicas de listas en Python: agregar elementos,
contar apariciones, indexar, hacer slicing, concatenar y buscar
si un valor esta contenido en una lista.
"""

# --- Lista de numeros enteros ---
numeros_enteros = [1, 2, 3, 4, 5, 5, 5, 2, 1, 1, 6]
nombres = ['Mauri', 'George', 'Stalder']

numeros_enteros.append(6)
print(numeros_enteros)

# Acceder al primer elemento (indice 0)
print(numeros_enteros[0])

# Contar cuantas veces aparece el 5 en la lista
print('Cantidad de 5s')
print(numeros_enteros.count(5))

# --- Slicing y concatenacion de listas ---
lista_a = [10, 21, 2, -6]

# lista_a[1:3] toma los elementos desde el indice 1 hasta el 2 (el 3 no se incluye)
print(lista_a[1:3])

lista_b = [2, 5]
print(lista_a + lista_b)

nueva_lista = lista_a + lista_b
print(nueva_lista)

# Verificar si el 5 esta presente en la lista resultante
print(5 in nueva_lista)
