# crear una función lambda que tome como parámetro una frase y la escriba al revés

parametro = input ("Por favor, ingresá una frase: ")

dar_vuelta = lambda parametro: parametro [::-1]

print (dar_vuelta (parametro))