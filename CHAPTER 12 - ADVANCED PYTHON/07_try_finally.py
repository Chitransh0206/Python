try:
    a = int(input("Hey, Enter a number: "))
    print(a)

 
except Exception as e:
    print(e)     #Here program is not crashed , it will print the error message and continue running.

finally:
    print("Hey, I am inside else.")    #IN FINALLY IT WILL RUN ON BOTH THE CASES , WHETHER THE EXCEPTION OCCUR OR NOT.
#IT IS MAINLY USED IN FUNCTION, IF RETURN IS THEIR IN STATEMENTS THEN NON PRINT STATEMENT WILL NOT BE EXECUTED, BUT THE FINALLY WILL BE EXECUTED.


# def main():
# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)
#     return
 
# except Exception as e:
#     print(e)     
#     return

#     print("Hey, I am inside else.")   #HERE THIS PRINT STATEMENT WILL NOT RUN IN BOTH THE CASES

# main()