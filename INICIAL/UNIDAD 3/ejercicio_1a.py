# Tome el ejercicio de cálculo de números pares e impares de la unidad 2 
# y agréguele un bucle al código de forma de simplificarlo. 

import sys

# Verifico que el usuario haya pasado 3 argumentos
if len(sys.argv) != 3:
    print("⚠️ Algo salió mal. Tenés que pasar sólo tres parámetros. Volvé a intentarlo.")
else:
    # Guardo los argumentos en variables
    numero_1 = int(sys.argv[1])
    numero_2 = int(sys.argv[2])
    numero_3 = int(sys.argv[3])

    # Verifico que cada número sea múltiplo de 2 y muestro el resultado
    for numero in [numero_1, numero_2, numero_3]:
        if numero % 2 == 0:
            print(f"{numero} es múltiplo de 2 ✅")
        else:
            print(f"{numero} no es múltiplo de 2 ❌")