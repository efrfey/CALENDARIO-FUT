def leer_entrada (lectura_datos):
    """
    Lee un archivo de entrada y devuelve la matriz de distancias, 
    el valor mínimo y máximo.
    """
    with open(lectura_datos, 'r', encoding='utf-8-sig') as archivo:
        lineas = archivo.readlines()

    n = int(lineas[0].strip())  # Número de equipos
    matriz_distancias = []

    # Leer la matriz de distancias
    for i in range(1, n + 1):
        fila = list(map(int, lineas[i].strip().split()))
        matriz_distancias.append(fila)

    # Leer los valores Min y Max
    Min = int(lineas[n + 1].strip())
    Max = int(lineas[n + 2].strip())

    return  matriz_distancias,Min,Max
