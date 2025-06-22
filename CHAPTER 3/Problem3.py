#Write a program to detect double space in a string.

name = "Harry is a good boy"
print(name.find("  "))  # This will return -1 if no double space is found, otherwise it will return the index of the first occurrence of double space

name1 = "Harry is a  good boy "
print(name1.find("  "))  # This will return the index of the first occurrence of double space, which is 10 in this case

name1 = "Harry is a good boy "
print(name1.find("goo"))

