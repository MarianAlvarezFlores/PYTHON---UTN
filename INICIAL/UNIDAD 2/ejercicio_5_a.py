# Escriba un programa que solicite el perímetro. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# LONGITUD = 2 * π * radio
#L = Longitud de perímetro
#π = Número pí igual a 3.1416
#r = Radio 
#usa una funcion de forma qie la operacion se realice dentro de la misma

# Defino la función que calcula el perímetro del círculo

def calcular_perimetro_circulo(radio):
    """Calcula el perímetro de un círculo"""
    PI = 3.1416
    longitud_perimetro = 2 * PI * radio
    return longitud_perimetro

# Solicito el radio del círculo por consola

radio_circulo = float(input("Por favor, ingresá el radio del círculo: "))

# Calculo el perímetro usando la función

perimetro_circulo = calcular_perimetro_circulo(radio_circulo)

# Muestro el resultado en la terminal

print(f"El perímetro del círculo es: {perimetro_circulo}")