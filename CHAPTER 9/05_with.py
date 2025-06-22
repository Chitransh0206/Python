# f = open("file.txt")
# print(f.read())
# f.close()

# THE SAME CAN BE WRITTEN USING WITH STATEMENT LIKE THIS:

with open("file.txt") as f:    # here their is no need to close the file by f.close while using WITH
    f.read()
    print(f.read())
    #You don't have to explicitly close the file