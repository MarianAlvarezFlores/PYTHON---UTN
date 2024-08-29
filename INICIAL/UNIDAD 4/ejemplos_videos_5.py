# Asignación de argumentos

def por_posicion (x, y, z):
    print (x, y, z)

por_posicion (1, 2, 3)

def por_nombre (x, y, z):
    print (x, y, z)

por_nombre ( x=1, y=2, z=3)

# cuando no sé qué cantidad parámetros que voy a tomar:

def f (a, *args): # cuando llame a f y le pase muchos parámetros. el primero lo va a tomar por posición y los demás como tupla.
                 #esa tupla puede ser recorrida por un for
    for arg in args:
        print (arg) 

def f_2 (**kwargs): #permite args pero en diccionario
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print (clave, "==>", valor)
