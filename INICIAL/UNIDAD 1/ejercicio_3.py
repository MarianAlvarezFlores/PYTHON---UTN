# Escriba un programa que solicite el perímetro. Presente el resultado en la terminal del editor.
#Utilice la siguiente fórmula:
# L = Longitud de perímetro
# L = 2 · π · r
# π = Número pí igual a 3.1416
# r = Radio

# Defino pi

PI = 3.1416

# Le pedimos al / a la usuario/a 

radio = int (input ("Ingresá el valor del radio: "))

# Calculamos el perímetro usando la fórmula L = 2 * pi * r

perimetro = 2 * PI * radio

# Presentamos el resultado

print("El perímetro es:", perimetro)