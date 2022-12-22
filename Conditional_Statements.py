# a = int(input("enter Your age"))
# print("Your Age Is :", a)

# Conditional operator
# > , <, >= , <= , == , !=

# if Else
# if(a>18):
#     print("You can drive")
# else:
#     print("you cannot drive")


#elif


# num = int(input("Enter The Value of Num : "))

# if(num<0):
#     print("Number is Negative")
# elif(num==0):
#     print("num is Zero")
# else:
#     print("Number is positive")


#Nested if

num = 10

if(num==0):
    print("Number is negative")
elif(num > 0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is Less than 20")
else:
    print("Number is zero")
