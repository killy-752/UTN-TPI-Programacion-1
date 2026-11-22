def actualizar_stock(inventario):
    """Registra una venta (resta unidades) o un ingreso (suma unidades) de una herramienta existente.
    Si el inventario está vacío, la herramienta no existe o el movimiento es inválido, lo informa.
    Si un dato es inválido o la venta supera el stock, lanza ValueError, que captura main()."""
    fue_herramienta_encontrada = False
    herramienta_encontrada = None

    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre_herramienta = input("Ingrese el nombre de la herramienta que desea actualizar: ").strip()

    if nombre_herramienta == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for herramienta in inventario:
        if herramienta["herramienta"].lower() == nombre_herramienta.lower():
            fue_herramienta_encontrada = True
            # Apunta al diccionario que ya está en inventario (no es una copia),
            # así que modificar su 'cantidad' actualiza el inventario directamente
            herramienta_encontrada = herramienta

    if not fue_herramienta_encontrada:
        print(f"La herramienta {nombre_herramienta} no se encuentra en el inventario.")
        return

    opcion_actualizacion_stock = input(
        "Ingrese 1 para registrar una venta o 2 para registrar un ingreso de mercadería: "
    ).strip()

    if opcion_actualizacion_stock != "1" and opcion_actualizacion_stock != "2":
        print("La opción ingresada es incorrecta.")
        return

    cantidad_a_actualizar = int(input("Ingrese la cantidad de unidades (mayor a 0): ").strip())

    if cantidad_a_actualizar <= 0:
        raise ValueError("La cantidad de unidades debe ser mayor a 0.")

    if opcion_actualizacion_stock == "1":
        if herramienta_encontrada['cantidad'] < cantidad_a_actualizar:
            raise ValueError("No hay suficientes unidades para completar esta venta.")

        herramienta_encontrada['cantidad'] -= cantidad_a_actualizar
    elif opcion_actualizacion_stock == "2":
        herramienta_encontrada['cantidad'] += cantidad_a_actualizar

    print(
        f"Stock actualizado: {herramienta_encontrada['herramienta']} "
        f"ahora tiene {herramienta_encontrada['cantidad']} unidades."
    )
