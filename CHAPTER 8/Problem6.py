# Write a python function which converts inches to cms. 

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter length in inches: "))
print(f"{n} inches is {inch_to_cms(n):.2f} cm")  # Output formatted to 2 decimal places
# ANOTHER WAY OF LAST LINE:  print(f"{round(inch_to_cms(n), 2)} cm")  # This will round the result to 2 decimal places.