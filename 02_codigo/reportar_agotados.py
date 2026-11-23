def reportar_agotados(inventario):
    """Muestra las herramientas con stock 0. Informa si el inventario está vacío
    o si ninguna herramienta está agotada."""
    hay_productos_sin_stock = False

    if len(inventario) == 0:
        print("No hay productos en el inventario.\n")

    for producto in inventario:
        if producto["cantidad"] == 0:
            # Imprime el encabezado solo antes del primer agotado
            if not hay_productos_sin_stock:
                print("========Productos agotados=========")

            hay_productos_sin_stock = True
            print(producto["herramienta"])

    if len(inventario) > 0 and not hay_productos_sin_stock:
        print("No hay productos agotados.\n")
