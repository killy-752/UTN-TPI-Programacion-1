def reportar_agotados(inventario):
    hay_productos_sin_stock = False

    if len(inventario) == 0:
        print("No hay productos en el inventario.")

    for producto in inventario:
        if producto["cantidad"] == 0:
            if not hay_productos_sin_stock:
                print("========Productos agotados=========")

            hay_productos_sin_stock = True
            print(producto["herramienta"])

    if len(inventario) > 0 and not hay_productos_sin_stock:
        print("No hay productos agotados.")
