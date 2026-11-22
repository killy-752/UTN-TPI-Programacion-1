def validacion_enteros_positivos(n,bool):
    """bool define si la función va a incluir el 0 como número válido (True) o no (False)"""

    try:
        n = int(n)

        if n == 0 and bool:
            return True

        if n <= 0 and not bool:
            raise ValueError("Su número es incorrecto. Ingrese un número mayor a cero.")

        if n <=0 and bool:
            raise ValueError("Su número es incorrecto. Ingrese un número mayor a cero.")
        
        return n
                
    except ValueError:
        print("Ha ingresado un valor incorrecto. Intente nuevamente.")

def validar_eleccion_menu(numero):
    """Función para validar la elección en el menú principal."""
    try:
        numero=int(numero)
        return numero
    except ValueError:
        numero=0
        print("Ha ingresado un valor no válido. Intente nuevamente.")
        return 0



        