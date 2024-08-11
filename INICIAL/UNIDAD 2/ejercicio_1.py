#Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
#pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
#son múltiplos de dos. Utilice la estructura if/else

import sys

# Verifico que usuario/a haya pasado 3 argumentos

if len(sys.argv) != 4:
    print("⚠️ Algo salió mal. Tenés que pasar sólo tres parámetros. Volvé a intentarlo")
else:
    # Paso los args a int
    numero1 = int(sys.argv[1])
    numero2 = int(sys.argv[2])
    numero3 = int(sys.argv[3])

    # Verifico que cada número sea múltiplo de 2 y muestro el resultado

    if numero1 % 2 == 0:
        print(f"{numero1} es múltiplo de 2 ✅")
    else:
        print(f"{numero1} no es múltiplo de 2 ❌")

    if numero2 % 2 == 0:
        print(f"{numero2} es múltiplo de 2 ✅")
    else:
        print(f"{numero2} no es múltiplo de 2 ❌")

    if numero3 % 2 == 0:
        print(f"{numero3} es múltiplo de 2 ✅")
    else:
        print(f"{numero3} no es múltiplo de 2 ❌")