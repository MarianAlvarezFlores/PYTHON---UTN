# A partir del ejerció 6 cree un programa con 4 funciones:
#alta() para dar de alta la nueva compra
#baja() para dar de baja una compra
#consulta() para consultar por todas las compras realizadas hasta el momento
#modificar() para modificar una compra realizada

# Defino una lista vacía para las compras

lista_compras = []

# Función alta 

def alta_compra (compra):
    """Permite dar de alta una compra"""
    lista_compras.append(compra)
    print(f"✅ Se agregó '{compra}' a la lista de compras.")

def baja_compra ():
    """Permite dar de baja una compra"""
    lista_compras.clear  
    print(f"Se vació tu carrito 🛒")

def consulta_compra ():
    """Permite consultar los productos en el carrito"""
    if len (lista_compras) > 0:
        print (f"🛒En tu carrito tenes: {lista_compras}")
    else:
        print (f"Tu carrito está vacío 😔")

def modificar_compra():
    """Permite modificar un producto en el carrito"""
    if len(lista_compras) > 0:
        print("En tu carrito hay:")
        for indice, valor in enumerate(lista_compras):
            print(f"{indice}: {valor}")

        # Solicitar al usuario el índice del elemento a modificar
        indice_modificar = input("Ingresá el índice del elemento que querés modificar: ")
                # Verificar que el índice es un número
        if indice_modificar.isdigit():
            indice_modificar = int(indice_modificar)

            # Verifico que el índice esté dentro del rango de la lista
            if 0 <= indice_modificar < len(lista_compras):
                # Solicito el nuevo valor
                nuevo_valor = input("Ingresá el nuevo valor: ")

                # Modifico el elemento en la lista
                lista_compras[indice_modificar] = nuevo_valor

                # Muestro la lista actualizada
                print("Tu nueva lista tiene:")
                for indice, valor in enumerate(lista_compras):
                    print(f"{indice}: {valor}")
            else:
                print("⚠️ Índice inexistente. No se realizó ninguna modificación.")
        else:
            print("⚠️ Debes ingresar un número válido.")
    else:
        print("Tu carrito está vacío, no hay nada para modificar 😔")

def menu ():
     while True:
        opcion = input("Hola, bienvenido/a al sistema de compras de la verdulería. ¿Qué querés hacer hoy?\n"
                       "1. Hacer una compra\n"
                       "2. Vaciar el carrito\n"
                       "3. Consultar tu carrito\n"
                       "4. Modificar tu carrito\n"
                       "5. Salir\n"
                       "Selecciona una opción (1-5): ")
        if opcion == '1':
            compra = input("Ingrese el nombre del producto a agregar: ")
            alta_compra(compra)
        elif opcion == '2':
            baja_compra()
        elif opcion == '3':
            consulta_compra()
        elif opcion == '4':
            modificar_compra()
        elif opcion == '5':
            print("Gracias por usar el sistema de compras de la verdulería. ¡Hasta luego! 👋")
            break
        else:
            print("⚠️ Opción no válida, por favor ingrese un número del 1 al 5.")
menu ()