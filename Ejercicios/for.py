for i in range(1,5):
    print(i)
else:
    print("Se termino el loop")
    
for i in range(2,8,2):
    print(i)
else:
    print("se termino el segundo loop")
    
for i in list(range(6)):#imprime del 0 al 5
    print(i)
else:
    print("se termino el tercer loop")
    
while True:
    s = input("Enter something: ")
    if s == "quit":
        break
    print("Length of the string is:", len(s))
print("Done!!!\n")