try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Invalid input. Please enter a valid number.")
    print(v)
except Exception as e:
    print(e)     #Here program is not crashed , it will print the error message and continue running.

print("Thank You!")    