
from cargar_productos import cargar_productos
from validacion import validar_eleccion_menu
from visualizacion import visualizar
from consultar_stock import consultar_stock


#Software de inventario.

#Bucle Main

inventario=[]

while True:


    texto_menu = "Bienvenido al softare de inventario para ferreterías MarFlo \n Ingrese la opción deseada: \n" \
    "[1]. Cargar productos. \n" \
    "[2]. Visualización. \n" \
    "[3]. Consulta de stock. \n" \
    "[4]. Reporte de agotados. \n" \
    "[5]. Alta de nuevo producto. \n" \
    "[6]. Actualizar stock. \n" \
    "[7]. Salir del programa. \n" \

    eleccion=input(texto_menu)
    eleccion=validar_eleccion_menu(eleccion)

    try:
        match eleccion:
            case 1:
                try:
                    inventario=cargar_productos(inventario)
                except:
                    continue
            case 2:
                visualizar(inventario)
            case 3:
                consultar_stock(inventario)
            case 7:
                print("Gracias por utilizar el servicio de seguimiento MarFlo 1.0. ¡Buenos días!")
                input()
            case _:
                raise ValueError   
    except ValueError:
        print("La opción ingresada está fuera del rango permitido. Intente nuevamente. \n")
