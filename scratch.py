# Definimos la matriz 3x3
matriz = [
    [9, 4, 7],
    [2, 8, 1],
    [6, 5, 3]
]

# Algoritmo Bubble Sort para ordenar una lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        print(f"Fila original {fila}: {matriz[fila]}")
        matriz[fila] = bubble_sort(matriz[fila])
        print(f"Fila ordenada  {fila}: {matriz[fila]}")
    else:
        print("Número de fila fuera de rango.")

# Ejemplo: ordenar la fila 1 (segunda fila, índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz completa después de ordenar
print("Matriz resultante:")
for fila in matriz:
    print(fila)
