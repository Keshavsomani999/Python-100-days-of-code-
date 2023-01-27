class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is  {self.name}")

class Programmer(Employee):
    def showlamguage(self):
        print(f"the defalt {self.name} python")


e = Employee("Rohan",420)
e.showDetails()

e2 = Programmer("Keshav",200)

e2.showlamguage()