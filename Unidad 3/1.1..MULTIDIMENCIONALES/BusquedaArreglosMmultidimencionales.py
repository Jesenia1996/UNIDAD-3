
def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posicion (fila, columna)
    return None  # Retorna None si no se encuentra el valor

# Definimos una matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor a buscar
valor_a_buscar = 50
resultado = buscar_en_matriz(matriz, valor_a_buscar)

if resultado:
    print(f"El valor {valor_a_buscar} se encontro en la posicion: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontro en la matriz.")
