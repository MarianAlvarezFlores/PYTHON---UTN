# isinstance(x, list) permite consultar si el elementos x es del tipo lista.
# A partir de la siguiente función recursiva que permite
#lista = ["elemento1n1", "elemento2n1", "elemento3n1",
#["elemento1n2", "elemento2n2", "elemento3n2",
#["elemento1n3", "elemento2n3", "elemento3n3"]]]
#def recorre_lista(item):
#for x in item:
#if isinstance(x, list):
#recorrer_lista(x)
#else:
#print(x)
#recorrer_lista(lista)

#Optimice el código de forma que el programa considere:

# Un valor de lista por defecto
# Permita tomar un segundo parámetro que lleve un registro del nivel en el que se encuentra (en qué grado del anidamiento)
# Permita tomar un valor por defecto de cero para el parámetro anterior.
# Presente la salida según el siguiente formato:

#elemento1n1
#elemento2n1
#elemento3n1
   #elemento1n2
   #elemento2n2
   #elemento3n2
     #elemento1n3
     #elemento2n3
     #elemento3n3

def recorrer_lista (item, nivel = 0) :
    """Permite recorrer elementos y niveles de la lista"""

    i = 1  # cuento los items
    for x in item :
        if isinstance (x, list) :
            print( "     " * nivel + f"Nivel: {nivel}, Item: {i}:")
            recorrer_lista(x, nivel + 1)
        else:
            print("     " * nivel + f"Nivel {nivel}, Item {i}: {x}")
        i += 1  # incremento la cuenta de los ítems

# Lista de la consigna para probar la función

lista = ["elemento1n1", "elemento2n1", "elemento3n1",
         ["elemento1n2", "elemento2n2", "elemento3n2",
          ["elemento1n3", "elemento2n3", "elemento3n3"]]]

recorrer_lista(lista)