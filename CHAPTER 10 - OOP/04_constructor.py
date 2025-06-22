class Employee:
    language = "Python"    #This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):    #here underscores are double at each side these are called DUNDER METHODS-methods which are called automatically.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):   #HAM KOI BHI METHOD BNAYE USE SELF DENA PADTA HE CHAHE USE KRE YA NA KRE
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning!")    

harry = Employee("Harry", 1300000, "JavaScript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)        

# rohan = Employee()