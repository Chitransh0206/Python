#What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

s = set()  # Using a set to store unique values
s.add(20)  # Adding an integer
s.add(20.0)  # Adding a float, which is considered the same as the integer 20
s.add('20')  # Adding a string, which is different from the integer and float
print(len(s))  # Output: 2