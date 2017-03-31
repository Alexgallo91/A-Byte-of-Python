i = int(input("ingresa un numero:\n"))
running = True

while running:
    guess = int(input("Numero a adivinar:"))
    
    if i == guess:
        print("Felicidades, lo adivinaste")
        running = False
    elif guess < i:
        print("El numero es mucho mas grande")
    else:
        print("El numero es mucho mas chico")
else:
    print("Se termino el loop")
