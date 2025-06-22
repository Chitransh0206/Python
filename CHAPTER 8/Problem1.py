# Write a program using functions to find greatest of three numbers. 

def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = 1    
b = 2
c = 3
print(f"The greatest of {a}, {b}, and {c} is: {greatest(a, b, c)}")
# This program defines a function to find the greatest of three numbers and prints the result.