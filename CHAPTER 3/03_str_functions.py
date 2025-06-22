name = "Harry"
print(len(name))  # Output: 5

# ends with
print(name.endswith("rry"))  # Output: True

#starts with
print(name.startswith("Har"))  # Output: True
print(name.startswith("har"))  # Output: False

# capitalize
print(name.capitalize())  # Output: "Harry" it capitalizes the first letter and lowercases the rest

# string replace
print(name.replace("ar", "ra"))  # Output: "Hrary"