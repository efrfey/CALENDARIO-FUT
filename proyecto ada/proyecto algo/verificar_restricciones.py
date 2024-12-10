def verificar_restricciones(calendario, Min, Max):
    """
    Verifica si un calendario cumple con las restricciones de tamaño mínimo y máximo 
    para giras (partidos consecutivos como visitante) y permanencias (partidos consecutivos como local).
    
    :param calendario: Matriz de calendario (resultado de generar_calendario).
        - Filas: Fechas del calendario.
        - Columnas: Equipos.
        - Valores positivos: El equipo juega como visitante contra el valor absoluto del número.
        - Valores negativos: El equipo juega como local contra el valor absoluto del número.
    :param Min: Tamaño mínimo permitido para las giras y permanencias.
    :param Max: Tamaño máximo permitido para las giras y permanencias.
    :return: 
        - True si el calendario cumple con las restricciones de giras y permanencias.
        - False si no las cumple.
    """
    n = len(calendario[0])  # Número de equipos
    
    for equipo in range(n):  # Iterar sobre cada equipo
        conteo = 0
        estado_actual = None  # Puede ser 'local' o 'visitante'
        
        print(f"\nVerificando equipo {equipo+1}")
        
        for fecha in range(len(calendario)):  # Recorrer cada fecha
            partido = calendario[fecha][equipo]
            partido = calendario[fecha][equipo]
            
            # Determinar si el equipo está jugando como visitante o local
            nuevo_estado = 'visitante' if partido > 0 else 'local'
            
            print(f"Fecha {fecha+1}: Partido {'Visitante' if nuevo_estado == 'visitante' else 'Local'}")
            
            # Si no se ha asignado un estado aún, asignamos el primero
            if estado_actual is None:
                estado_actual = nuevo_estado
                conteo = 1
            # Si el estado sigue siendo el mismo, incrementamos el conteo
            elif nuevo_estado == estado_actual:
                conteo += 1
            else:  # Cambió de estado (de local a visitante o viceversa)
                # Verificar si la secuencia anterior cumple con las restricciones
                if conteo < Min or conteo > Max:
                    print(f"Restricción violada! - Estado: {estado_actual}, Conteo: {conteo}")
                    return False  # Si no cumple con las restricciones, retorna False
                estado_actual = nuevo_estado  # Actualizar estado
                conteo = 1  # Reiniciar el conteo para la nueva secuencia
        
        # Verificar la última secuencia al finalizar todas las fechas
        if conteo < Min or conteo > Max:
            print(f"Restricción violada en última secuencia! - Estado: {estado_actual}, Conteo: {conteo}")
            return False  # Si no cumple con las restricciones, retorna False

    return True  # Si no se encontraron violaciones de restricciones, retorna True