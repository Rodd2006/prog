from functools import reduce
# Queremos:
#   1. Filtrar solo las compras que superan los $50.
#   2. Aplicarles un descuento del 10% a esas compras seleccionadas.
#   3. Sumar un impuesto del 21% (IVA) a cada una.
#   4. Calcular cuánto dinero total hay que cobrar.

# ==============================================================================
# Inmutabilidad
# ==============================================================================
# Inmutabilidad: Usamos una tupla () en lugar de lista []. Los datos originales
# quedan intactos como un registro o comprobante que nadie puede alterar.
PRECIOS_COMPRAS = (20.0, 60.0, 100.0, 15.0, 80.0,60.0)


# ==============================================================================
# FUNCIONES PURAS Y DE ORDEN SUPERIOR
# ==============================================================================

def es_compra_importante(precio: float) -> bool:
    """Función Pura: Solo responde si el precio es mayor a 50. 

    No cambia nada fuera de ella y siempre responde lo mismo si le das el mismo valor.
    """
    return precio > 50.0


def crear_calculador_precio_final(descuento: float, impuesto: float):
    """Función de Orden Superior y Clausura (Closure):

    Es una fábrica que "construye" una nueva función personalizada. 
    Recibe el porcentaje de descuento e impuesto, y devuelve una función lista para usar.
    """
    def transformar(precio: float) -> float:
        # 1. Aplica descuento
        precio_con_descuento = precio * (1.0 - descuento)
        # 2. Agrega impuesto
        precio_final = precio_con_descuento * (1.0 + impuesto)
        return precio_final

    return transformar


def sumar_totales(acumulado: float, precio_actual: float) -> float:
    """Función Pura: Toma dos valores y devuelve su suma."""
    return acumulado + precio_actual


# ==============================================================================
# PROCESAMIENTO DECLARATIVO 
# ==============================================================================

# Creamos nuestra herramienta de cálculo personalizada: 10% descuento (0.10) y 21% IVA (0.21)
calcular_final_10_21 = crear_calculador_precio_final(
    descuento=0.10, impuesto=0.21
)

# PASO 1: FILTER (Colador)
# Conserva solo los precios que cumplen la condición (> 50)
compras_filtradas = filter(es_compra_importante, PRECIOS_COMPRAS)

# PASO 2: MAP (Transformador)
# Le aplica la transformación (descuento + IVA) a cada elemento filtrado
compras_procesadas = map(calcular_final_10_21, compras_filtradas)

# PASO 3: REDUCE (Acumulador)
# Junta todos los elementos transformados y los reduce a un solo valor sumándolos
total_a_cobrar = reduce(sumar_totales, compras_procesadas, 0.0)


# ==============================================================================
# PRESENTACIÓN DE RESULTADOS
# ==============================================================================
print("=== DEMOSTRACIÓN DE PARADIGMA FUNCIONAL ===")
print(f"Precios de compras originales: {PRECIOS_COMPRAS}")
print(f"Total final a cobrar:          ${total_a_cobrar:.2f}")

# Demostración de inmutabilidad:
print(f"\n¿Cambiaron los precios originales?: {PRECIOS_COMPRAS}")