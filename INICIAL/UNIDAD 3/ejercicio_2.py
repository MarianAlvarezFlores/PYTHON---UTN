# Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 

# Le pido al usuario que escriba una oración

oracion = input("Por favor, escribí una oración: ").lower() 

# Cuento la cantidad de letras "a" en la oración

cantidad_a = oracion.count("a")

# Muestro el resultado al usuario

print(f"En tu oración la letra 'a' aparece {cantidad_a} veces.")
      