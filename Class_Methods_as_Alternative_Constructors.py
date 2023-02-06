class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

# alternative constructor
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])


# e = Employee("harry",12000)
# print(e.name)
# print(e.salary)

string = "Harry-12000"
e1 = Employee.fromStr(string)
print(e1.name)
print(e1.salary)
