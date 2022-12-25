def gmean(a,b): 
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

a= 9
b=8
isGreater(a,b)
gmean(a,b)

c= 8
d = 7
isGreater(c,d) # calling function c,d is a parameter
gmean(c,d)

