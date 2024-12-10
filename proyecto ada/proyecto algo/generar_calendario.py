import random

def generar_calendario(n, Min, Max):
    """
    Genera un calendario inicial para un torneo todos contra todos ida y vuelta.
    """
    fechas_totales = 2 * (n - 1)
    calendario = [[None for _ in range(n)] for _ in range(fechas_totales)]
    
    equipos = list(range(1, n + 1))
    random.shuffle(equipos)

    for i in range(n - 1):
        for j in range(n // 2):
            equipo_local = equipos[j]
            equipo_visitante = equipos[-(j + 1)]
            calendario[i][equipo_local - 1] = equipo_visitante
            calendario[i][equipo_visitante - 1] = -equipo_local

        equipos = [equipos[0]] + equipos[-1:] + equipos[1:-1]

    for i in range(n - 1, fechas_totales):
        for j in range(n):
            if calendario[i - (n - 1)][j] is not None:
                calendario[i][j] = -calendario[i - (n - 1)][j]

    return calendario