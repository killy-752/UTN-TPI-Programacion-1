def visualizar(inventario):

    if inventario:
        print("Se registran las siguientes herramientas:")
        for posicion in range(len(inventario)):
            for key , value in inventario[posicion].items():
                print(f"{key}:" , str(value).title())
    else:
        print("===== No hay herramientas cargadas en el sistema. ===== \n")
        