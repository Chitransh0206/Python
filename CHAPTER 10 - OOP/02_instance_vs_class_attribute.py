class Employee:
    language = "Python"    #This is a class attribute
    salary = 1200000

    def getInfo(self):   #HAM KOI BHI METHOD BNAYE USE SELF DENA PADTA HE CHAHE USE KRE YA NA KRE
        print(f"The language is {self.language}. The salary is {self.salary}.")

harry = Employee()
harry.language = "JavaScript"     #This is a instance attribute
# harry.getInfo()    THIS LINE WILL WORK SAME AS THE LINE GIVEN BELOW
Employee.getInfo(harry)


# def greet():
#     print("Good Morning!")

# harry.greet()    NOT VALID
# harry.greet(self)  VALID    