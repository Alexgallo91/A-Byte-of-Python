while True:
    s = input("Ingresa lo que sea:")
    if s == "quit":
        break
    if len(s) < 3:
        print("too small")
        continue
    print("tiene buena longitud la cadena")