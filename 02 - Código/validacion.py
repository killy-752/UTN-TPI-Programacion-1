def validacion_enteros_positivos(n,bool):
    """bool define si la función va a incluir el 0 como número válido (True) o no (False)"""

    try:
        n = int(n)

        if n <= 0 and not bool:
            raise ValueError("Su número es incorrecto. Ingrese un número mayor a cero.")

        return n
                
    except ValueError:
        print("Ha ingresado un valor incorrecto. Intente nuevamente.")

        