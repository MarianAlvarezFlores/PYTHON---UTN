# realice un programa que consulte la edad  y en que caso que el valor ingresado 
# #supere la fecha de jubilación presente en la terminal el mensaje "ya está en edad de jubilarse"
# caso contrario que presente "aún está en la edad de trabajar".

EDAD_JUBILACION_MUJER = 60
EDAD_JUBILACION_HOMBRE = 65

# Consulto el género

genero = input("Por favor, ingresa tu género (hombre/mujer): ").strip().lower()

# Consulto la edad

edad = int(input("Ingresa tu edad: "))

condicion_1 = (genero == "hombre") and (edad >= EDAD_JUBILACION_HOMBRE)
condicion_2 = (genero == "mujer") and (edad >= EDAD_JUBILACION_MUJER)

if condicion_1 or condicion_2:
    print ("Tiene edad para jubilarse")
else:
    print ("Aún está en edad de trabajar")