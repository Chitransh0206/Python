# Write a program to find the maximum of the numbers in a list using the reduce 
# function. 

from functools import reduce

l = [1, 2, 343, 53, 241, 425, 754, 45, 55]

def greater(a, b):
    if (a > b):
        return a
    return b

print(reduce(greater, l))