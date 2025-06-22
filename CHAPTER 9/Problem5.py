# Repeat program 4 for a list of such words to be censored. 

words = ["Donkey", "bad", "ganda"]

with open("files.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("files.txt", "w") as f:  
    f.write(content)