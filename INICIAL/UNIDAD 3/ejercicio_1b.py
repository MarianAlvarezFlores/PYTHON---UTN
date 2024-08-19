# Tome el ejercicio de cálculo de números pares e impares de la unidad 2 (en verdad está en la U1)
# y agréguele un bucle al código de forma de simplificarlo. 

import sys

# Verifico que se hayan pasado los tres parámetros 

if len(sys.argv) != 4:
    print("⚠️ Ups. Algo salió mal. Tenés que proporcionar exactamente tres parámetros.")
else:
    for i in range(1, 4):
        valor = int(sys.argv[i])
        if valor % 2 == 0:
            print(f"El número {valor} es par ✅")
        else:
            print(f"El número {valor} es impar ❌")
