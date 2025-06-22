# PROJECT 1: SNAKE, WATER, GUN GAME 
# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user.

'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1, -1, 0])  # Randomly choose between snake, water, and gun
youstr = input("Enter your choice (snake(s)/water(w)/gun(g)): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"You chose: {reverseDict[you]}\nComputer choose {reverseDict[computer]}")


if(computer == -1 and you == 1):
    print("You win! Snake beats Water")
elif(computer == -1 and you == -1):
    print("It's a tie! Both chose Water")
elif(computer == -1 and you == 0):
    print("You lose! Water beats Gun")
elif(computer == 0 and you == 1):
    print("You lose! Gun beats Snake")
elif(computer == 0 and you == -1):
    print("You win! Snake beats Gun")
elif(computer == 0 and you == 0):
    print("It's a tie! Both chose Gun")
elif(computer == 1 and you == 1):
    print("It's a tie! Both chose Snake")
elif(computer == 1 and you == -1):
    print("You lose! Snake beats Water")
elif(computer == 1 and you == 0):
    print("You win! Water beats Gun")
else:
    print("Invalid input! Please enter snake, water, or gun.")


# BELOW LOGIC IS WRITTEN ON THE BASIS OF THE VALUE OF COMPUTER - YOU    

# if((computer - you) == -1 or (computer - you) == 0):
#     print("You lose!")
# else:
#     print("You win!")

