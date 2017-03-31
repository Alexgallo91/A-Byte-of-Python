number = 23
guess = int(input("Enter an integer : "))

if guess == number:
    #new block starts here
    print("Congratulations, you guessed it.")
    print("(but you don not win any prizes!)")
elif guess < number:
    #Another Block
    print("No, it is a little higher than that")
    #you can do whatever you want in a Block
else:
    print("No, it it a little lower than that")
    
    
print("Done")