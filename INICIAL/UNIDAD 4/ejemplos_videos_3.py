nivel_0 = 0

def f1 ():
    nivel_1 = 1

    def f2 ():
        nivel_2 = 2
        print (nivel_0, nivel_1, nivel_2)
    
    f2 ()
    print (nivel_0, nivel_1)



f1 ()
print (nivel_0)