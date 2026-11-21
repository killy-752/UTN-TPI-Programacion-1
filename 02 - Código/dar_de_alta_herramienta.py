def dar_de_alta_herramienta(inventario):
    nombre_nueva_herramienta = input("Ingrese el nombre de la herramienta que desea agregar al inventario: ").strip()

    if nombre_nueva_herramienta == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre_nueva_herramienta.lower():
            raise ValueError(f"La herramienta '{herramienta['herramienta']}' ya está cargada en el inventario.")

    cantidad_nueva_herramienta = int(input(f"Ingrese el stock inicial de {nombre_nueva_herramienta} (0 o más unidades): ").strip())

    if cantidad_nueva_herramienta < 0:
        raise ValueError("El stock no puede ser negativo.")

    inventario.append({'herramienta': nombre_nueva_herramienta, 'cantidad': cantidad_nueva_herramienta})
