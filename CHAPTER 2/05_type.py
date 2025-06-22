a = 31
t= type(a)
print(t)  # <class 'int'>

b = 3.14
t = type(b)
print(t)  # <class 'float'>

c = "Hello, World!"
t = type(c)
print(t)  # <class 'str'>

d = "3.14"
t = type(d)
print(t)  # <class 'str'>, even though it looks like a float

e = "31.2"
f = float(e)  # Convert string to float
t = type(f) # Now f is a float
print(t)  # <class 'float'>