#Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()  # Using a set to store unique values
s.add(18)  # Adding an integer
s.add('18')  # Adding a string
print(s)  # Display the set with both values 