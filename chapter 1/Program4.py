# Write a program to print the contents of a directory using the os module.
# Search online for the function which does that.

import os

# Specify the path of the directory
path = '.'  # '.' refers to the current directory

# Get the list of files and directories
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
