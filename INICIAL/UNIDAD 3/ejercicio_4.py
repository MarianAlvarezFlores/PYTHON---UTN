# Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido. 

# Solicito la edad al usuario/a

edad = int(input("Por favor, ingresá tu edad: "))

# Verifico que haya ingresado una edad válida

if edad < 0:
    print("🚫La edad no puede ser negativa.")
else:
    # Imprimo todos los años que la persona cumplió
    print("🎉 Años cumplidos: ")
    for año in range(1, edad + 1):
        print(año)