# A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.

print("¡Bienvenido/a al sistema de compras de la verdulería 🍎🥕!")

entrada = input("Ingresá 'c' para comenzar o 'f' para finalizar: ")

diccionario_compras = {}
total = 0

if entrada == 'c':
   valor = True
else:
    valor = False

while valor == True:
    producto, cantidad, precio = input("Ingresá el producto, la cantidad y el precio con espacios: ").split()
    cantidad = float(cantidad)
    precio = float(precio)
    total += cantidad * precio 

    diccionario_compras[producto] = {
        'cantidad': cantidad,
        'precio': precio
    }

    entrada = input("Si deseas agregar otro producto escribí 'a'. Para finalizar escribí 'f': ")
    valor = (entrada == 'a')

print("🛒 Compras realizadas:")
for producto in diccionario_compras.items():
    print(f"{producto}: Cantidad {cantidad}. Precio unitario: $ {precio}")

print(f"El total a pagar es: ${total:.2f}")