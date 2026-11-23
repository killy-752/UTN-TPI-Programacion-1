# inventario=[{"herramienta":"1","cantidad":2}]

def consultar_stock(inventario):

    if inventario:

        herramienta_existente=False

        print("Búsqueda de stock por nombre:")
        eleccion = str(input("Ingrese la herramienta a visualizar:")).strip().lower()
        
        try:
            if eleccion == "":
                raise ValueError("")
        except ValueError:
            print("El valor nombre ingresado no puede estar vacío.")

        for posicion in range(len(inventario)):
            if inventario[posicion]["herramienta"] == eleccion:
                herramienta_existente=True
                print(f"El stock de {str(eleccion).title()} es de {inventario[posicion]['cantidad']} unidades.")

        if not herramienta_existente:
            print("La herramienta seleccionada no está ingresada en el sistema.")

    else:
        print("===== No hay herramientas cargadas en el sistema. ===== \n")

# consultar_stock(inventario)
        