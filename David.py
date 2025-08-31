# Definimos la matriz 3x3
matriz = [
    [5, 8, 3],
    [1, 7, 9],
    [4, 6, 2]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):         # Recorre filas
        for j in range(len(matriz[i])):  # Recorre columnas
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Valor a buscar
valor_buscado = 9

# Llamada a la función
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)
