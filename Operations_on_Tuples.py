# change item in tuple in indirect way

# contries = ("india","spain","Italy","England")

# temp = list(contries)
# temp.append("Russia")
# temp.pop(3)
# temp[2]="Finland"
# contries = tuple(temp)
# print(contries)

tuple1 = (0,1,2,9,2,3,1,3,2)

# res = tuple1.count(3) # 3 will come in how many times in tuple1
#res = tuple1.index(3) #accurence of 3 in tuple 1
# res = tuple1.index(3,6,8) # by slicing
res = len(tuple1)
print(res)