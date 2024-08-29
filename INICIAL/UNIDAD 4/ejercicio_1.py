# Cree una función lamba que compruebe si un número es par o impar

es_par = lambda numero : f"{numero} es par" if numero % 2 == 0 else f"{numero} es impar"

# lo pruebo

resultado = es_par (2)
print (resultado)

resultado = es_par (5)
print (resultado)