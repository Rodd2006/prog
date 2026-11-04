from functools import reduce
from typing import Callable, Iterable, Generator

# ==============================================================================
# 1. FUNCIONES PURAS, INMUTABILIDAD Y EFECTOS SECUNDARIOS
# ==============================================================================

# Inmutabilidad: Usamos una tupla de datos inicial que jamás se modifica.
DATOS_ORIGINALES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def es_par(n: int) -> bool:
    """Función pura: sin efectos secundarios y determinista."""
    return n % 2 == 0

def duplicar(n: int) -> int:
    """Función pura: no altera ninguna variable externa."""
    return n * 2


# ==============================================================================
# 2. FUNCIONES COMO VALORES Y FUNCIONES DE ORDEN SUPERIOR
# ==============================================================================

# Una función asignada a una variable (Función como valor)
operacion_duplicar = duplicar

def crear_multiplicador(factor: int) -> Callable[[int], int]:
    """Higher-Order Function: Recibe/devuelve otra función (ver Clausuras)."""
    def multiplicar(n: int) -> int:
        return n * factor
    return multiplicar


# ==============================================================================
# 3. COMPOSICIÓN DE FUNCIONES, CLAUSURAS (CLOSURES) Y RECURSIÓN
# ==============================================================================

# Clausura (Closure): triplicar conserva el valor del ámbito léxico (factor = 3).
triplicar = crear_multiplicador(3)

def componer(f: Callable, g: Callable) -> Callable:
    """Composición de funciones: h(x) = f(g(x))."""
    return lambda x: f(g(x))

# h(x) primero triplica y luego duplica
triplicar_y_duplicar = componer(duplicar, triplicar)

def factorial_recursivo(n: int) -> int:
    """Recursión: Repetición de cómputo sin bucles ni estados mutables."""
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)


# ==============================================================================
# 4. TRANSFORMACIONES DE COLECCIONES CON map, filter Y reduce
# ==============================================================================

# 1. filter: Filtra los números pares de la tupla original
pares = filter(es_par, DATOS_ORIGINALES)

# 2. map: Aplica la función de composición a los elementos filtrados
transformados = map(triplicar_y_duplicar, pares)

# 3. reduce: Acumula/suma todos los elementos resultantes en un único valor
suma_total = reduce(lambda acc, x: acc + x, transformados)


# ==============================================================================
# 5. EVALUACIÓN ESTRICTA Y PEREZOSA (LAZY EVALUATION)
# ==============================================================================

def generador_infinito_perezoso() -> Generator[int, None, None]:
    """Evaluación Perezosa: Produce valores a demanda usando un generador."""
    num = 1
    while True:
        yield num  # No calcula ni almacena en memoria hasta ser solicitado
        num += 1


# ==============================================================================
# 6. COINCIDENCIA DE PATRONES (PATTERN MATCHING) Y TIPOS ALGEBRAICOS
# ==============================================================================

def procesar_expresion(expresion: tuple) -> str:
    """Pattern Matching (match/case) para simular estructuras algebraicas de datos."""
    match expresion:
        case ("Sumar", a, b):
            return f"Resultado de la suma: {a + b}"
        case ("Multiplicar", a, b):
            return f"Resultado de la multiplicación: {a * b}"
        case ("Texto", mensaje):
            return f"Mensaje: {mensaje.upper()}"
        case _:
            return "Operación no reconocida"


# ==============================================================================
# DEMOSTRACIÓN Y SALIDA
# ==============================================================================

if __name__ == "__main__":
    print("--- 1, 2 & 4. Transformaciones con map, filter y reduce ---")
    print(f"Datos originales (Inmutables): {DATOS_ORIGINALES}")
    print(f"Suma total procesada: {suma_total}")

    print("\n--- 3. Clausuras, Composición y Recursión ---")
    print(f"Composición triplicar_y_duplicar(2): {triplicar_y_duplicar(2)}")
    print(f"Factorial recursivo de 5: {factorial_recursivo(5)}")

    print("\n--- 5. Evaluación Perezosa ---")
    gen = generador_infinito_perezoso()
    # Solo tomamos los primeros 3 valores calculados a demanda
    primeros_tres = [next(gen), next(gen), next(gen)]
    print(f"Primeros 3 elementos consumidos bajo demanda: {primeros_tres}")

    print("\n--- 6. Pattern Matching ---")
    print(procesar_expresion(("Sumar", 10, 20)))
    print(procesar_expresion(("Texto", "paradigma funcional")))