# Write a python program using function to convert Celsius to Fahrenheit. 

def f_to_c(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


f = int(input("Enter temperature in F: "))
print(f"{f} F is {f_to_c(f):.2f} C")       # Here :.2f formats the output to 2 decimal places.

# ANOTHER WAY OF LAST LINE:  print(f"{round(f_to_c(f), 2)} C")  # This will round the result to 2 decimal places.