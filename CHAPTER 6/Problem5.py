#Write a program to find whether a given username contains less than 10 
# characters or not. 

l = ["Harry", "Ron", "Hermione", "Draco", "Neville"]

name = input("Enter your name: ")

if name in l:
    print("Welcome to the wizarding world, " + name + "!")

else:
    print("You are not a wizard, " + name + ".")
    print("Please try again with a valid wizard name.")