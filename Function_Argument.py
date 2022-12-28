# def average(a=9,b=1):
#     print("The Average is " , (a+b)/2)

# # average(5,5) required arguments
# # average() it take a and b default argument
# average(1,5)

# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum = sum+i
#     print("average is: " , sum/len(numbers))

# average(5,4,3,5)  #We take Infinite arguments


def name(**name):
    return "Hello ",name["fname"],name["mname"],name["lname"]


c = name(fname = "keshav",lname="Somani",mname="ji")
print(c)