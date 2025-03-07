def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]  # Intercambiar

# Defino una matriz 3x3
matriz = [
    [9, 2, 3],
    [4, 8, 6],
    [7, 1, 5]
]

# Muestro la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordeno la segunda fila (índice 1)
bubble_sort(matriz[1])

# Muestro la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz:
    print(fila)