def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number to calculate its factorial: "))
result = factorial(n)    
print(f"The factorial of {n} is: {result}")
# This code defines a recursive function to calculate the factorial of a number.