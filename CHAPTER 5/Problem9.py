#Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}
# No, you cannot include a list inside a Python set, because lists are mutable (changeable) and unhashable — and sets require all their elements to be hashable and immutable.
# This will raise a TypeError because lists are mutable and cannot be added to a set

s = {8, 7, 12, "Harry", (1, 2)}  # Using a tuple instead of a list

s[4][0] = 10  # Attempting to change the first element of the tuple
# This will raise a TypeError because tuples are immutable and cannot be changed

#If you need to store something like [1, 2] in a set, convert it to a tuple (which is immutable):
s = {8, 7, 12, "Harry", (1, 2)}
# Now you can access the elements of the tuple, but you cannot change them