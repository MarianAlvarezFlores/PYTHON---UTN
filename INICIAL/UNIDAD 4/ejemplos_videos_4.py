nivel_0 = 0

def f1 ():
    nivel_1 = 1

    def f2 ():
        nonlocal nivel_1 # nivel_1 no es global pero tampoco local. variable del tipo no local. Definida en nivel intermedio.
        nivel_1 = 7
        nivel_2 = 2
        print (nivel_0, nivel_1, nivel_2)
    
    f2 ()
    print (nivel_0, nivel_1)



f1 ()
print (nivel_0)