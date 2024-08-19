# A partir del ejerció 7 cree un programa con 4 funciones:
# alta() para dar de alta la nueva compra
# baja() para dar de baja una compra
# consulta() para consultar por todas las compras realizadas hasta el momento
# modificar() para modificar una compra realizada
# Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios

# Variables globales
diccionario_compras = {}
total = 0

def alta ():
    """Sirve para dar de alta una compra"""
    global total
    producto, cantidad, precio = input("Ingresá el producto, la cantidad y el precio separados por espacios: ").split()
    cantidad = float(cantidad)
    precio = float(cantidad)
    total += cantidad * precio

    diccionario_compras[producto] = {
        'cantidad': cantidad,
        'precio': precio
    }

def baja ():
    """Sirve para dar de baja un producto"""
    global total
    producto = input ("Ingresá el nombre del producto que querés eliminar: ")

    if producto in diccionario_compras:
        total -= diccionario_compras [producto] ['cantidad'] * diccionario_compras [producto] ['precio']
        del diccionario_compras [producto]
        print (f"{producto} eliminado correctamente")
    else :
        print (f"El producto {producto} no está en el carrito ❌")

def consulta ():
    """Sirve para consultar los productos que hay en el carrito de compras"""
    print("🛒 Compras realizadas:")
    for producto, detalles in diccionario_compras.items ():
        print (f"{producto}: cantidad {detalles ['cantidad']}. Precio unitario: $ {detalles ['precio']:.2f}")
        print(f"El valor total de tu compra es de: ${total}")

def modificar ():
    """Sirve para modificar una compra del carrito"""
    global total
    producto = input("Ingresá el nombre del producto que querés modificar: ")

    if producto in diccionario_compras:
        cantidad_nueva, precio_nuevo = input ("Ingresá la nueva cantidad y el nuevo precio separado por espacios: ").split()
        cantidad_nueva= float (cantidad_nueva)
        precio_nuevo = float (precio_nuevo)

        total -= diccionario_compras [producto] ['cantidad'] * diccionario_compras [producto] ['precio']
        total += cantidad_nueva * precio_nuevo

        diccionario_compras [producto] = {
            'cantidad' : cantidad_nueva,
            'precio' : precio_nuevo
        }

        print(f"Producto '{producto}' lo modificaste con éxito ✅")
    else:
        print(f"El producto '{producto}' no está en el carrito ❌")

print("¡Bienvenido/a al sistema de compras de la verdulería 🍎🥕!")

entrada = input("Ingresá 'c' para comenzar o 'f' para finalizar: ")

if entrada == 'c':
    valor = True
else:
    valor = False

while valor:
    accion = input("Elegí una acción: alta ('a'), baja ('b'), consulta ('c'), modificar ('m'), finalizar ('f'): ").lower()

    if accion == 'a': 
        alta()
    elif accion == 'b':
        baja()
    elif accion == 'c':
        consulta()
    elif accion == 'm':
        modificar()
    elif accion == 'f':
        valor = False
    else:
        print ("❌ La opción que elegiste es incorrecta")