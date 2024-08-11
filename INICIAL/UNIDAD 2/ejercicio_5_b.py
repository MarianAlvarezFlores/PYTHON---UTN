# Escriba un programa que solicite el radio de una circunferencia y permita calcular el área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
#𝐴 = 𝜋. 𝑟ଶ
#A = Área 
#π = Número pi igual a 3.1416
#r = Radio 

# Defino la función para calcular el área de la circunferencia

def calcular_area_circunferencia(radio):
    """Calcula el área de una circunferencia"""
    PI = 3.1416
    area = PI * (radio ** 2)
    return area

# Le pido al usuario/a el radio de la circunferencia 

radio_circunferencia = float(input("Por favor, ingresá el radio: "))

# Calculo el área usando la función

area_circunferencia = calcular_area_circunferencia(radio_circunferencia)

# Muestro el resultado en la terminal

print(f"El área de la circunferencia es: {area_circunferencia:.2f}")