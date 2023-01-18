# def double(x):
#     return x*2


def appl(fx,value):
    return 6 + fx(value)


double = lambda x: x*2
cube = lambda x: x*x*x
print(double(5))

# output :   10

sum = lambda x,y: (x+y)

print(sum(5,4))


print(appl(cube,2))