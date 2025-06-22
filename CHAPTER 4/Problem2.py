#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = int(input(f"Enter marks for student {i + 1}: "))  #Here int is for converting input to integer and if we not use it, input will be string
    marks.append(mark)

print("Marks before sorting:", marks)
marks.sort()  # Sorting the list of marks
print("Marks after sorting:", marks)    