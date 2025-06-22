#  Write a program to print multiplication table of n using for loops in reversed 
# order.

n = int(input("Enter a number to print its multiplication table in reversed order: "))

# for i in range(10, 0, -1):
#     print(f"{n} x {i} = {n * i}")

# ANOTHER GOOD METHOD

for i in range(1, 11):
    print(f"{n} x {11 - i} = {n * (11 - i)}")