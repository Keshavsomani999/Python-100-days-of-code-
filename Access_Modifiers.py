# Access Specifiers/Modifiers

# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

# Let us see the each one of access specifiers in detail:

# Types of access specifiers

# 1. Public access modifier

# 2. Private access modifier

# 3. Protected access modifier


# Default public
# class Employee:
#     def __init__(self):
#         self.name = "Harry"


# a = Employee()
# print(a.name)



class Employee:
    def __init__(self):
        self.__name = "Keshav"


a = Employee()
# print(a.__name) # we can not access directly __name


# Name mangling
print(a._Employee__name) # can be access indirectly  


