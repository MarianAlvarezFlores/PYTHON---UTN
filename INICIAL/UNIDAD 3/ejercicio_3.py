# Escriba un programa que consulte al usuario por una oración 
# y comente al usuario cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  

# Le pido al usuario/a que ingrese una oración

oracion = input ("Por favor escribí una oración: ").lower()

# Defino las vocales que deberán ser contadas

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú",
           "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]

# Cuento la repitencia de cada vocal en la oración y solo muestro las que se utilizaron

for vocal in vocales:
    cantidad = oracion.count(vocal)
    if cantidad > 0:
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")