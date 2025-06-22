#Check that tuple type cannot be changed in python.

a = (1, 45, 352, 3424, False, "Rohan", "Shivam")  # Creating a tuple
a[2] = "New Value"  # Attempting to change an element in the tuple
# This will raise a TypeError because tuples are immutable