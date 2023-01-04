tup = (1,2,6,7,"green") # Tuple don't change

print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

if 2 in tup:
    print("Yes present")


tup2 = tup[1:3]
print(tup2)