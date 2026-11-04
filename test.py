from functools import reduce

# Datos iniciales (Inmutables)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11)

# 1. Funciones puras (mismo input genera siempre el mismo output, sin efectos secundarios)
def es_impar(x: int) -> bool:
    return x % 2 != 0

def duplicar(x: int) -> int:
    return x * 2

def sumar(acumulador: int, valor: int) -> int:
    return acumulador + valor

# 2. Transformaciones de colecciones usando filter, map y reduce
impares = filter(es_impar, numeros)         # Filtra los números impares: (1, 3, 5, 7, 9)
duplicados = map(duplicar, impares)        # Aplica la función duplicar: (2, 6, 10, 14, 18)
total = reduce(sumar, duplicados, 0)       # Acumula y suma todos los valores: 50

print(f"Resultado final: {total}")  # 50