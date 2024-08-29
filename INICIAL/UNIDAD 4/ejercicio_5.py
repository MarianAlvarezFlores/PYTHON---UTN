# Cree un programa que utilizando una función, solicite la edad de la persona e imprima
#todos los años que la persona ha cumplido según el siguiente formato de ejemplo.
#1, 2, 3, 4, 5
#Y
#5, 4, 3, 2, 1

def mostrar_anos_cumplidos(edad):
    """Sirve para mostrar todos los años cumplidos en sentido descendente y ascendente """
    print (", ".join(str(año) for año in range(1, edad + 1)))
    print (", ".join(str(año) for año in range(edad, 0, -1)))


edad = int(input("Por favor, ingresá tu edad: "))
mostrar_anos_cumplidos (edad)
