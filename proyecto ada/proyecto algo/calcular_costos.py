def calcular_costos(calendario, matriz_distancias):
    """
    Calcula el costo total de un calendario en función de la matriz de distancias.

    :param calendario: Matriz del calendario (filas = fechas, columnas = equipos).
    :param matriz_distancias: Matriz de distancias entre los equipos.
    :return: El costo total del calendario.
    """
    costo_total = 0

    # Recorrer las fechas del calendario
    for fecha in calendario:
        for equipo, partido in enumerate(fecha):
            if partido is not None:  # Si hay un partido para este equipo
                equipo_local = equipo
                equipo_visitante = abs(partido) - 1  # Ajustar índice (si parte desde 1)
                
                # Asegurarse de que no se salga de rango en la matriz
                if equipo_local < len(matriz_distancias) and equipo_visitante < len(matriz_distancias[equipo_local]):
                    costo_total += matriz_distancias[equipo_local][equipo_visitante]

    return costo_total