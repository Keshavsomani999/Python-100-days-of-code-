class Emoployee:
    companyName = "Apple"
    noOfEmployee= 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Emoployee.noOfEmployee +=1
    def showDetails(self):
        print(f"The name is : {self.name} and raise amount is {self.raise_amount} in {self.companyName} total employee {self.noOfEmployee}" )

# Emoployee.showDetails("keshav")
emp = Emoployee("keshav")
emp.raise_amount = 0.3
emp.companyName = "Apple India"
Emoployee.companyName ="Google"
emp.showDetails()
emp1 = Emoployee("harry")
emp1.showDetails()