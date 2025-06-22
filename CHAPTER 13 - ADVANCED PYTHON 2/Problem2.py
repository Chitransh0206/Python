# Write a program to input name, marks and phone number of a student and format it 
# using the format function like below:

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Phone number: "))

# f string is more easier but here we use format function
s = "The name of the student is {}, his marks are {} and his phone number is {}".format(name, marks, phone)
print(s)