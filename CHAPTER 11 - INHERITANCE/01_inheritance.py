#BASE/PARENT CLASS
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language.")
#NOT A GOOD METHOD AS FOR IMPLEMENTING A CHANGE IN SO MANY SIMILAR CLASSES IT WILL TIME CONSUMING AND ERROR PRONE            

#SAME PROGRAM-SHORT AND EFFICIENT
#INHERITED CLASS
class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
