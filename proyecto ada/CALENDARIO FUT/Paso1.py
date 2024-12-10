def leer_entrada(archivo):
    with open(archivo, 'r') as file:
        # Leer el número de equipos
        n = int(file.readline().strip())
        # Leer los valores mínimos y máximos de gira/permanencia
        min_gira = int(file.readline().strip())
        max_gira = int(file.readline().strip())
        # Leer la matriz de distancias
        matriz_distancias = []
        for _ in range(n):
            fila = list(map(int, file.readline().strip().split()))
            matriz_distancias.append(fila)
    return n, min_gira, max_gira, matriz_distancias

# Ejemplo de uso
archivo_entrada = "entrada.txt"  # Nombre del archivo con datos
n, min_gira, max_gira, matriz_distancias = leer_entrada(archivo_entrada)

print("Número de equipos:", n)
print("Tamaño mínimo de gira:", min_gira)
print("Tamaño máximo de gira:", max_gira)
print("Matriz de distancias:")
for fila in matriz_distancias:
    print(fila)
