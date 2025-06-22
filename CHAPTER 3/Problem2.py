#  Write a program to fill in a letter template given below with name and date .

letter = """Dear <|NAME|>,
         You are selected!
         <|DATE|> """
print(letter.replace("<|NAME|>", "Harry").replace("<|DATE|>", "1st January 2025"))