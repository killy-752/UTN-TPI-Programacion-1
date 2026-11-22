from cargar_productos import cargar_productos
from validacion import validar_eleccion_menu
from visualizacion import visualizar
from consultar_stock import consultar_stock
from reportar_agotados import reportar_agotados
from alta_herramienta import alta_herramienta
from actualizar_stock import actualizar_stock


# Software de inventario.

# Funcion principal que crea el inventario y lo pasa por parámetro a cada opción
def main():
    inventario = []


    while True:

        texto_menu = (
            "Bienvenido al software de inventario para ferreterías MarFlo \n Ingrese la opción deseada: \n"
            "[1]. Cargar productos. \n"
            "[2]. Visualización. \n"
            "[3]. Consulta de stock. \n"
            "[4]. Reporte de agotados. \n"
            "[5]. Alta de nuevo producto. \n"
            "[6]. Actualizar stock. \n"
            "[7]. Salir del programa. \n"
        )
        eleccion = input(texto_menu)
        eleccion = validar_eleccion_menu(eleccion)

        try:
            match eleccion:
                case 1:
                    try:
                        inventario = cargar_productos(inventario)
                    except:
                        continue
                case 2:
                    visualizar(inventario)
                case 3:
                    consultar_stock(inventario)
                case 4:
                    reportar_agotados(inventario)
                case 5:
                    alta_herramienta(inventario)
                case 6:
                    actualizar_stock(inventario)
                case 7:
                    print("Gracias por utilizar el servicio de seguimiento MarFlo 1.0. ¡Hasta luego!")
                    break
                case _:
                    raise ValueError("La opción ingresada está fuera del rango permitido. Intente nuevamente.")
        except ValueError as e:
            print(f"Error: {e}")

# Punto de entrada donde inicia el programa
main()
