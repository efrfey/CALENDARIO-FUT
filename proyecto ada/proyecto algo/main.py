from lectura_datos import leer_entrada
from generar_calendario import generar_calendario
from calcular_costos import calcular_costos
from verificar_restricciones import verificar_restricciones

print("Leyendo datos de entrada...")
matriz_distancias, Min, Max = leer_entrada("entrada.txt")
print("Datos leídos:")
print("Matriz de distancias:")
for fila in matriz_distancias:
    print(fila)
print(f"Min: {Min}, Max: {Max}")

print("\nGenerando calendario...")
calendario = generar_calendario(len(matriz_distancias), Min,Max)
for fila in calendario:
    print(fila)

print("\nCalculando costos...")
costo_total = calcular_costos(calendario, matriz_distancias)
print(f"Costo total del calendario: {costo_total}")

print("\nVerificando restricciones...")
cumple_restricciones = verificar_restricciones(calendario, Min, Max)
if cumple_restricciones:
    print("El calendario cumple con las restricciones.")
else:
    print("El calendario no cumple con las restricciones.")