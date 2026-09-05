"""
Demuestra que 'range' no devuelve una lista, sino un objeto
'range' que genera los numeros a medida que se los recorre.
Para ver los elementos hay que convertirlo con list().
"""

numero = 5

print(numero)

# Esto imprime "range(0, 5)", no los numeros del 0 al 4
print(range(numero))

# Para ver los numeros que genera hay que convertirlo a lista
print(list(range(numero)))
