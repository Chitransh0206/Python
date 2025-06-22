# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

#     @property
#     def name(self):
#         return self.ename 

#     @name.setter
#     def name(self, value):
#         self.ename = value

# e = Employee()
# e.a = 45      
# e.name = "Harry"
# print(e.name)  

# e.show()



class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self): 
        return f"{self.fname} {self.lname}" 

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45      
e.name = "Harry Khan"      #USER WILL INPUT WHOLE NAME
print(e.fname, e.lname)    #USER KO NHI PATA LGEGA KI USKA FIRST AUR LAST NAME ALAG ALAG SAVE HO RAHA HE
#THIS IS THE CONCEPT BEHIND ENCAPSULATION AND ABSTRACTION
e.show()