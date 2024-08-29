# Global - local

a= 5 #variable global
b= 6

def nopisa ():
    global a
    a = 10     #variable local
    print (a, b)

nopisa()
print (a)