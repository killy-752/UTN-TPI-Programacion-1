
from cargar_productos import cargar_productos
from validacion import validar_eleccion_menu

#Software de inventario.

#Bucle Main

while True:

    inventario = []
    eleccion=0

    texto_menu = "Bienvenido al softare de inventario para ferreterías MaFlo \n Ingrese la opción deseada: \n" \
    "[1]. Cargar productos. \n" \
    "[2]. Visualización. \n" \
    "[3]. Consulta de stock. \n" \
    "[4]. Reporte de agotados. \n" \
    "[5]. Alta de nuevo producto. \n" \
    "[6]. Actualizar stock. \n" \
    "[7]. Salir del programa. \n" \

    eleccion=input(texto_menu)
    eleccion=validar_eleccion_menu(eleccion)

    match eleccion:
        case 0:
            continue
        case 1:
                try:
                    inventario=cargar_productos(inventario)
                except:
                    continue

