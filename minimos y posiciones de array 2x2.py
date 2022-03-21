productos = [[285,300,290,284.99],[559,560,565,560],[82,85,80,79]]
NUM_PRODUCTOS = 3
NUM_PROVEEDORES = 4


def calcularPrecioPromedioDeProducto(producto):
    suma = 0
    if producto == 0:
        for i in range(NUM_PROVEEDORES):
            suma += productos[0][i]
        promedio = suma/NUM_PROVEEDORES
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)
    elif producto == 1:
        for i in range(NUM_PROVEEDORES):
            suma += productos[1][i]
        promedio = suma/NUM_PROVEEDORES
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)
    elif producto == 2:
        for i in range(NUM_PROVEEDORES):
            suma += productos[2][i]
        promedio = suma/NUM_PROVEEDORES
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)

def calcularPrecioPromedioDeProveedor(proveedor):
    suma = 0
    if proveedor == 0:
        for i in range(NUM_PRODUCTOS):
            suma += productos[i][0]
        promedio = suma/NUM_PRODUCTOS
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)

    elif proveedor == 1:
        for i in range(NUM_PRODUCTOS):
            suma += productos[i][1]
        promedio = suma/NUM_PRODUCTOS
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)

    elif proveedor == 2:
        for i in range(NUM_PRODUCTOS):
            suma += productos[i][2]
        promedio = suma/NUM_PRODUCTOS
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)

    elif proveedor == 3:
        for i in range(NUM_PRODUCTOS):
            suma += productos[i][3]
        promedio = suma/NUM_PRODUCTOS
        promedio_redondeado = round(promedio, 2)
        return(promedio_redondeado)

def obtenerProveedorMasBarato(producto):
    if producto == 0:
        barato = []
        for i in range(NUM_PROVEEDORES):
            barato.append(productos[0][i])
        minimo = min(barato)
        posicion = barato.index(minimo)
        return(posicion)
    elif producto == 1:
        barato = []
        for i in range(NUM_PROVEEDORES):
            barato.append(productos[1][i])
        minimo = min(barato)
        posicion = barato.index(minimo)
        return(posicion)
    elif producto == 2:
        barato = []
        for i in range(NUM_PROVEEDORES):
            barato.append(productos[2][i])
        minimo = min(barato)
        posicion = barato.index(minimo)
        return(posicion)



if  __name__ ==  '__main__':
    for i in productos:
        print(i)
    print("Precio promedio de cada producto")
    for i in range(NUM_PRODUCTOS):
        print("Producto", i, "- Precio promedio:", "{0:.2f}".format(calcularPrecioPromedioDeProducto(i)))

       
    print("\nPrecio promedio cada proveedor")
    for j in range(NUM_PROVEEDORES):
        print("Proveedor", j, "- Precio promedio:", "{0:.2f}".format(calcularPrecioPromedioDeProveedor(j)))

       
    print("\nProveedor que vende cada producto más económicamente")
    for k in range(NUM_PRODUCTOS):
        print("Producto", k, "- Proveedor más económico =", obtenerProveedorMasBarato(k))
