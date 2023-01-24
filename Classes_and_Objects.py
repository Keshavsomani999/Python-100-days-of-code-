class Person:
    name = "Keshav"
    occ = "Software developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occ}")
    

a = Person()
# a.name = "shubam"
# print(a.name)
a.info()