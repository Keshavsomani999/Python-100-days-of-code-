class Person:
    # constructors
    def __init__(self,name,occ):
        print("i am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("KEshav","Hr")
b = Person("Divya","ceo")
c = Person()
a.info()
b.info()