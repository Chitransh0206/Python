# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F

marks = int(input("Enter the marks of the student: "))
if 90 <= marks <= 100:
    print("Grade: Ex")

elif 80 <= marks < 90:
    print("Grade: A")

elif 70 <= marks < 80:
    print("Grade: B")

elif 60 <= marks < 70:
    print("Grade: C")

elif (50 <= marks < 60):
    print("Grade: D")

elif (marks < 50):
    print("Grade: F")    

else:
    print("Invalid marks entered. Please enter a value between 0 and 100.")  
