# Cree un programa que incorpore el módulo sys, al cual desde la terminal
#  se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la 
# terminal si
# son múltiplos de dos. 

import sys

print(sys.argv)

"""
['ejercicio_2.py', '2', '3', '4']

"""

print("Si el valor de dividir por 2 da resto 0, entonces es par. Si no, es impar.")
var1 = int(sys.argv[1])
var2 = int(sys.argv[2])
var3 = int(sys.argv[3])

print("El número que ingresaste es: ", sys.argv[1], "El resto de dividir por 2 es: ", var1 % 2)
print("El número que ingresaste es: ", sys.argv[2], "El resto de dividir por 2 es: ", var2 % 2)
print("El número que ingresaste es: ", sys.argv[3], "El resto de dividir por 2 es: ", var3 % 2)