f = open("file.txt")

# lines = f.readlines()   #This readlines tells python to read all the lines in the file and store them in the variable lines.
# print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

f.close()


# ANOTHER EASY WAY
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()