a = int(input("Enter your age: "))

# if elif else ladder

if a < 0:
    print("Invalid age entered.")
elif a < 18:
    print("You are a minor.")
elif a == 18:
    print("You are just an adult.")
else:
    print("You are an adult.")
