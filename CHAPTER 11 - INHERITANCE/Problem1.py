# Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector. 

class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is ({self.x}x + {self.y}y)")


class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The vector is ({self.x}x + {self.y}y + {self.z}z)")    

a = TwoDVector(1, 2)        
a.show()
b = ThreeDVector(5, 2, 3)
b.show()