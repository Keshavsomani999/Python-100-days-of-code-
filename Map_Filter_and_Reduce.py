def cube(x):
    return x*x*x

l = [1,2,3,4,5,7]

# newl = []

# for item in l :
#     newl.append(cube(item))

# print(newl)

# output
# [1, 8, 27, 64, 125, 343]

# other way
# newl = list(map(cube,l))
# print(newl)
# output :[1, 8, 27, 64, 125, 343]

# def filter_function(a):
#     return a>4

# newnewl = list(filter(filter_function,l))

# print(newnewl)
# output  :   [5, 7]

from functools import reduce

number = [1,2,3,4,5]

def sum(x,y):
    return x+y

sum = reduce(sum,number)

print(sum)
# output : 15