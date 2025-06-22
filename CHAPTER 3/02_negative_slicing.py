name = "Harry"

print(name[-4:-1])  # Output: "arr"
# Negative slicing allows you to slice from the end of the string

print(name[:4])   # will trat as name[0:4]
print(name[1:])  # will treat as name[1:len(name)]

# Slicing with skip value
a = "0123456789"
print(a[1:7:3])  # Output: "14"
# The third parameter in slicing is the step, which allows you to skip characters