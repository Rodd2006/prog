from functools import reduce

# ==========================================
# INMUTABILIDAD
# ==========================================
PRECIOS_ORIGINALES = (20, 60, 100, 15, 80)


# ==========================================
# FUNCIONES PURAS
# ==========================================
def es_precio_mayor_a_50(precio: float) -> bool:
    """ evalúa una condición sin alterar nada."""
    return precio > 50

def sumar(a: float, b: float) -> float:
    """ suma dos valores y devuelve el resultado."""
    return a + b


# ==========================================
# FUNCIONES DE ORDEN SUPERIOR
# Una función que crea y devuelve otra función
# ==========================================
def crear_aplicador_descuento(porcentaje: float):
    """Devuelve una función ajustada al porcentaje indicado."""
    def aplicar(precio: float) -> float:
        return precio * (1 - porcentaje)
    return aplicar


# ==========================================
# TRANSFORMACIÓN DECLARATIVA DE COLECCIONES
# ==========================================

# 1. Creamos la función de descuento del 10% 
descuento_10 = crear_aplicador_descuento(0.1)

# 2. Filtrar precios > 50 
precios_filtrados = filter(es_precio_mayor_a_50, PRECIOS_ORIGINALES)

# 3. Transformar los precios filtrados aplicándoles el descuento 
precios_con_descuento = map(descuento_10, precios_filtrados)

# 4. Reducir la colección a un único valor sumando todos los precios
total_final = reduce(sumar, precios_con_descuento)


# ==========================================
# PRESENTACIÓN DE RESULTADOS
# ==========================================
print(f"Precios originales: {PRECIOS_ORIGINALES}")
print(f"Total procesado de forma funcional: ${total_final:.2f}")

# Comprobación de Inmutabilidad:
print(f"¿Los precios originales cambiaron?: {PRECIOS_ORIGINALES}")