# If the names of 2 friends are same; what will happen to the program in problem 6? 
# THE VALUES ENTERED LATER WILL BE UPDATED IN THE DICTIONARY.
# The program will still work, but the last entry for a friend's name will overwrite any previous entry with the same name.
d = {}

name =  input("Enter friend's name: ")
language = input("Enter friend's favorite language: ")
d.update({name: language})

name =  input("Enter friend's name: ")
language = input("Enter friend's favorite language: ")
d.update({name: language})

name =  input("Enter friend's name: ")
language = input("Enter friend's favorite language: ")
d.update({name: language})

name =  input("Enter friend's name: ")
language = input("Enter friend's favorite language: ")
d.update({name: language})

print(d)