def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento.
    
    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto es 10).
    
    Retorna:
    float: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
# Primera llamada: solo monto total
compra_1 = 200.0  # Monto total de la compra
descuento_1 = calcular_descuento(compra_1)
print(f"Descuento aplicado sobre {compra_1} con 10% de descuento: {descuento_1}")

# Segunda llamada: monto total y porcentaje de descuento
compra_2 = 150.0  # Monto total de la compra
porcentaje_2 = 15  # Porcentaje de descuento
descuento_2 = calcular_descuento(compra_2, porcentaje_2)
print(f"Descuento aplicado sobre {compra_2} con {porcentaje_2}% de descuento: {descuento_2}")
