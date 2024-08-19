# Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. 
# Realice un programa que tome de a uno la cantidad
#  y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. 

# Le doy la bienvenida a usuario/a

entrada = input ("Bienvenido/a al sistema de la verdulería 🍎🥕. Escribí: 'c' para comenzar, 'f' para finalizar: ")

total = 0

if entrada == 'c':
    valor = True
else:
    valor = False

while valor == True:
    producto, cantidad, precio = input("Ingresá el nombre y la cantidad del producto en kilos y el precio, separados por espacios: ").split()
    total = total + float(cantidad) * float(precio)
    entrada = input ("Para agregar otro producto, seleccioná 'a', para finalizar, seleccionar otro caracter: ")
    if entrada == 'a':
        valor = True
    else:
        valor = False

print("El valor total de la compra es de: ", total)