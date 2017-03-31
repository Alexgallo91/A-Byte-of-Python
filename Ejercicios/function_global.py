x = 50
numero = 1

def func():
    global x
    global numero
    
    print("x is", x)
    x = 2
    print("Changed global x to", x)
    
    numero += x 
    print("numero vale ahora", numero)
    
func()
print("Value of x is", x)
print("value of numero", numero)