def escribir_salida(archivo, n, min_gira, max_gira, calendario):
    with open(archivo, 'w') as file:
        # Escribir número de equipos
        file.write(f"{n}\n")
        # Escribir Min y Max
        file.write(f"{min_gira}\n")
        file.write(f"{max_gira}\n")
        # Escribir el calendario
        for fila in calendario:
            file.write(" ".join(map(str, fila)) + "\n")

# Ejemplo de uso
salida = "salida.txt"
calendario_ejemplo = [
    [3, 4, -1, -2],
    [2, -1, 4, -3],
    [4, -3, 2, -1],
    [-3, -4, 1, 2],
    [-2, 1, -4, 3],
    [-4, 3, -2, 1],
]

escribir_salida(salida, 4, 1, 3, calendario_ejemplo)
print(f"Archivo '{salida}' generado con éxito.")
