import itertools

def generar_calendarios(n):
    # Generar las combinaciones de equipos (ida y vuelta)
    equipos = list(range(1, n + 1))
    partidos = list(itertools.permutations(equipos, 2))  # Todas las combinaciones de ida
    calendario = list(itertools.permutations(partidos, n * (n - 1)))  # Todas las permutaciones posibles
    return calendario

# Validación inicial (calendarios válidos según las restricciones)
def es_calendario_valido(calendario, n, min_gira, max_gira):
    # Implementar reglas de validación aquí
    # Por ejemplo:
    # 1. Alternancia local/visitante
    # 2. Tamaños de giras y permanencias
    # 3. Sin repetición de partidos consecutivos
    return True  # Ajustar con la lógica específica

# Calcular el costo de un calendario
def calcular_costo(calendario, distancias):
    costo_total = 0
    for partido in calendario:
        local, visitante = partido
        costo_total += distancias[local - 1][visitante - 1]
    return costo_total

# Algoritmo ingenuo
def algoritmo_ingenuo(n, min_gira, max_gira, distancias):
    mejores_calendarios = []
    menor_costo = float('inf')

    # Generar todos los calendarios posibles
    calendarios_posibles = generar_calendarios(n)

    for calendario in calendarios_posibles:
        if es_calendario_valido(calendario, n, min_gira, max_gira):
            costo = calcular_costo(calendario, distancias)
            if costo < menor_costo:
                menor_costo = costo
                mejores_calendarios = [calendario]
            elif costo == menor_costo:
                mejores_calendarios.append(calendario)

    return mejores_calendarios, menor_costo

# Ejemplo de uso
n = 4
min_gira = 1
max_gira = 3
distancias = [
    [0, 745, 665, 929],
    [745, 0, 80, 337],
    [665, 80, 0, 380],
    [929, 337, 380, 0],
]

# Llamar al algoritmo
mejor_calendario, costo = algoritmo_ingenuo(n, min_gira, max_gira, distancias)
print("Mejor calendario:", mejor_calendario)
print("Costo total:", costo)
