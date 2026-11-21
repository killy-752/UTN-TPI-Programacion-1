from validacion import validacion_enteros_positivos as validar

inventario=[]

def cargar_productos(inventario):

    while True:

        cantidad_productos = input("Ingrese la cantidad de productos a cargar (debe ser mayor a cero) :")

        #Validación de datos

        cantidad_productos = validar(cantidad_productos,False)

        #Si la validación no es exitosa el objeto devuelto es None, por lo tanto 'not' nos deja continuar el bucle.

        if not cantidad_productos: 
            continue

        for n in range(cantidad_productos):

            inventario.append({'herramienta': "", 'cantidad': 0})
            herramienta_valida=False

            while not herramienta_valida:
                
                try:
                    herramienta=input(f"Ingrese el nombre de herramienta {n+1}:")
                    
                    if herramienta=="":
                        raise NameError

                    for posicion in range(len(inventario)):
                        # print("pos",posicion)
                        # print(len(inventario))
                        if herramienta in inventario[posicion].values():
                            raise ValueError
                except ValueError:
                    print("El producto ya está ingresado en el sistema. Intente nuevamente.")
                    continue
                except NameError:
                    print("Nombre inválido. No puede estar vacío. Intente nuevamente.")
                    continue


                
                herramienta_valida=True

            while True:
                herramienta_stock=input(f"Ingrese la cantidad de {herramienta} en stock.")
                herramienta_stock=validar(herramienta_stock,True)
                if type(herramienta_stock) == None:
                    continue
                else:
                    break
             
            inventario[len(inventario)-1]=({'herramienta': herramienta, 'cantidad': herramienta_stock})
            print(inventario)   

        return inventario
cargar_productos(inventario)

        

