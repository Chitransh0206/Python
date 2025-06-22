try:
    a = int(input("Hey, Enter a number: "))
    print(a)

 
except Exception as e:
    print(e)     #Here program is not crashed , it will print the error message and continue running.

else:
    print("I am inside else.")    #IF TRY BLOCK SUCCESFULLY EXECUTED THEN ONLY ELSE PART WILL OCCUR OTHERWISE NOT