marks = {
    "math": 95,
    "science": 88,
    "english": 23,
    0: "math"
}

print(marks.items())  # Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(marks.keys())   # Returns a view object that displays a list of all the keys in the dictionary
print(marks.values()) # Returns a view object that displays a list of all the values in the dictionary
marks.update({"math": 100, "history":95}) # Updates the value of the key "math" to 100 and adds a new key "history" with value 95
print(marks)

print(marks.get("math2"))  # Returns None if the key does not exist, instead of raising an error
#