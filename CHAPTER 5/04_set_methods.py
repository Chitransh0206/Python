s = {1,5,32,5,5,5,"Harry"}
print(s, type(s))  # {32, 1, 5, 'Harry'} - duplicates are removed, order is not guaranteed

s.add(566)  # Adds an element to the set
print(s, type(s))  # {32, 1, 5, 'Harry', 566}

s.remove(566)  # Removes an element from the set, raises KeyError if not found
print(s, type(s))  # {32, 1, 5, 'Harry'}

