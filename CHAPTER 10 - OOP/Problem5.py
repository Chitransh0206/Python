# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

# import random
from random import randint   #WE CAN USE THIS ALSO 

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        # print(f"Ticket fare in train no: {self.trainNo}
        # from {fro} to {to} is {random.randint(222, 5555)}")   IF IMPORT RANDOM IS USED

        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")   # WHEN from random import randint IS USED

t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")