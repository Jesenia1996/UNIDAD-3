# Calculo Descuento En Compras

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


def main():
    # Ejemplo 1: Llamada a la función con solo el monto total
    monto1 = 150.00  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Ejemplo 2: Llamada a la función con monto total y porcentaje de descuento
    monto2 = 200.00  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")


if __name__ == "__main__":
    main()



# EJEMPLO 2 DE LA TAREA
# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en base al monto total y el porcentaje de descuento dado.
    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
monto1 = 100  # Ejemplo de monto total de la compra
monto2 = 200  # Otro ejemplo de monto total
porcentaje_personalizado = 15  # Ejemplo de porcentaje de descuento diferente

# Llamadas a la función
monto_descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - monto_descuento1

monto_descuento2 = calcular_descuento(monto2, porcentaje_personalizado)
monto_final2 = monto2 - monto_descuento2

# Mostrar resultados
print(f"Compra 1: Monto total: ${monto1}, Descuento: ${monto_descuento1}, Monto final: ${monto_final1}")
print(f"Compra 2: Monto total: ${monto2}, Descuento: ${monto_descuento2}, Monto final: ${monto_final2}")
