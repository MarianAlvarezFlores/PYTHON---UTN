# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
# editor el valor incrementado en un 10%.
# tratando de utilizar una funcion de forma que la operacion se realice dentro de la misma.

# Defino la función que incrementa un valor en un 10%

def incrementar_valor(valor):
    incremento = 0.10 * valor
    valor_incrementado = valor + incremento
    return valor_incrementado

# Solicito al usuario un valor

valor_inicial = int(input("Por favor, ingresa un valor entero: "))

# Calculo el valor incrementado con la función

valor_incrementado = incrementar_valor(valor_inicial)

# Muestro el resultado

print(f"El valor incrementado en un 10% es: {valor_incrementado}")