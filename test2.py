from functools import reduce

# ==========================================
# PILAR 1: INMUTABILIDAD
# Usamos una tupla (o lista no modificada) como datos de entrada.
# ==========================================
PRECIOS_ORIGINALES = (20, 60, 100, 15, 80)


# ==========================================
# PILAR 2: FUNCIONES PURAS
# No modifican variables externas ni causan efectos secundarios.
# ==========================================
def es_precio_mayor_a_50(precio: float) -> bool:
    """Función pura: evalúa una condición sin alterar nada."""
    return precio > 50

def sumar(a: float, b: float) -> float:
    """Función pura: suma dos valores y devuelve el resultado."""
    return a + b


# ==========================================
# PILAR 3: FUNCIONES DE ORDEN SUPERIOR
# Una función que crea y devuelve OTRA función (Generador de descuentos)
# ==========================================
def crear_aplicador_descuento(porcentaje: float):
    """Devuelve una función ajustada al porcentaje indicado."""
    def aplicar(precio: float) -> float:
        return precio * (1 - porcentaje)
    return aplicar


# ==========================================
# PILAR 4: TRANSFORMACIÓN DECLARATIVA DE COLECCIONES
# Usamos filter, map y reduce sin recurrir a bucles explicitos (for/while)
# ==========================================

# 1. Creamos la función de descuento del 10% usando el Pilar 3
descuento_10 = crear_aplicador_descuento(0.1)

# 2. Filtrar precios > 50 (Pilar 4 + Pilar 2)
precios_filtrados = filter(es_precio_mayor_a_50, PRECIOS_ORIGINALES)

# 3. Transformar los precios filtrados aplicándoles el descuento (Pilar 4 + Pilar 3)
precios_con_descuento = map(descuento_10, precios_filtrados)

# 4. Reducir la colección a un único valor sumando todos los precios (Pilar 4 + Pilar 2)
total_final = reduce(sumar, precios_con_descuento)


# ==========================================
# PRESENTACIÓN DE RESULTADOS
# ==========================================
print(f"Precios originales: {PRECIOS_ORIGINALES}")
print(f"Total procesado de forma funcional: ${total_final:.2f}")

# Comprobación de Inmutabilidad:
print(f"¿Los precios originales cambiaron?: {PRECIOS_ORIGINALES}")