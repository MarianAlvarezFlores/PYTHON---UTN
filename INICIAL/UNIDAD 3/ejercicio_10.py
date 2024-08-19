# Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que esta sea correcta.
#  El programa debe informar al usuario si la contraseña fue correcta o no.  

# Le pido al usuario / a que ingrese una contraseña
contrasena_correcta = input("Definí una contraseña: ")

# Solicitar al usuario que ingrese la contraseña hasta que sea correcta

while True:
    contrasena_ingresada = input("Ingresá la contraseña: ")

    if contrasena_ingresada == contrasena_correcta:
        print("✅ Contraseña correcta")
        break
    else:
        print("❌ Contraseña incorrecta. Intentalo de nuevo.")