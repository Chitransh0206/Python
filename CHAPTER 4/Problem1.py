#Write a program to store 7 fruits in a list entered by the user.
fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)

print("List of fruits:", fruits)