# A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.

# Armo una lista vacía donde voy a ir guardando los datos

lista_compras = []

# Función para agregar las compras a la lista

def agregar_compra(compra):
    lista_compras.append(compra)

# Mensaje de bienvenida al usuario/a

print("¡Bienvenido/a al sistema de compras de la verdulería 🍎🥕!")

continuar = True
while continuar:
    compra = input("Ingrese el nombre de la compra (o 'salir' para terminar): ")
    if compra.lower() == 'salir':
        continuar = False
    else:
        agregar_compra(compra)

# Muestro la lista de las compras

print("\n🛒 Compras realizadas:")

if len(lista_compras) > 0:
    for item in lista_compras:
        print(f"✅ {item}")
else:
    print("No realizaste ninguna compra.")
