# Write a program to print the following star pattern: 
#    * 
#    ** 
#    ***      for n = 3

n = int(input("Enter the number of rows for the star pattern: "))
for i in range(1, n + 1):
    # Print stars
    print("*" * i)