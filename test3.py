from functools import reduce

# ==============================================================================
# 1. PROBLEMA Y DATOS DE ENTRADA (Inmutabilidad)
# ==============================================================================
#   1. Filtrar solo las notas aprobadas (mayores o iguales a 6).
#   2. Calcular la suma total de esas notas aprobadas.
#   3. Calcular el promedio de los aprobados sin modificar el registro original.
NOTAS_EXAMEN = (4.0, 7.0, 3.0, 9.0, 6.0, 10.0, 5.0)
# ==============================================================================
# 2. FUNCIONES PURAS
# ==============================================================================

def esta_aprobado(nota: float) -> bool:
    """Retorna True solo si la nota es >= 6.0."""
    return nota >= 6.0

def esta_desaprobado(nota: float) -> bool:
    """Retorna True solo si la nota es < 6.0."""
    return nota < 6.0

def sumar_notas(acumulado: float, nota_actual: float) -> float:
    """Suma la nota actual al total acumulado."""
    return acumulado + nota_actual

# ==============================================================================
# 3. TRANSFORMACIÓN DECLARATIVA (filter, reduce)
# ==============================================================================

# PASO 1: FILTER 
# Conserva solo las notas >= 6.0 (filtra 4.0, 3.0 y 5.0)
notas_aprobadas = tuple(filter(esta_aprobado, NOTAS_EXAMEN))
notas_desaprobadas = tuple(filter(esta_desaprobado, NOTAS_EXAMEN))

# PASO 2: REDUCE
# Suma todas las notas aprobadas hasta obtener una sola cifra total
suma_aprobados = reduce(sumar_notas, notas_aprobadas, 0.0)
suma_desaprobados = reduce(sumar_notas, notas_desaprobadas, 0.0)

# PASO 3: CÁLCULO FINAL (Función matemática sobre inmutables)
promedio_aprobados = suma_aprobados / len(notas_aprobadas)
promedio_desaprobados = suma_desaprobados / len(notas_desaprobadas)


print("=== SISTEMA DE CALIFICACIONES FUNCIONAL ===")
print(f"Todas las notas originales:  {NOTAS_EXAMEN}")
print(f"Notas aprobadas filtradas:   {notas_aprobadas}")
print(f"Suma de notas aprobadas:     {suma_aprobados}")
print(f"Promedio de nota de aprobados: {promedio_aprobados:.2f}")
print(f"Notas desaprobadas filtradas: {notas_desaprobadas}")
print(f"Suma de notas desaprobadas:   {suma_desaprobados}")
print(f"Promedio de nota de desaprobados:{promedio_desaprobados:.2f}")

# Comprobación de Inmutabilidad
print(f"\n¿Las notas originales cambiaron?: {NOTAS_EXAMEN}")