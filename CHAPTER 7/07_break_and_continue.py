for i in range(10):
    # Break the loop if i is 5
    if i == 5 :
        print("Breaking the loop at 5")   
        break      #Exit the loop right now
    print(i)

for i in range(10):
    # Continue the loop if i is even
    if i % 2 == 0:
        continue       #Skip the iteration if i is even
    print(i)