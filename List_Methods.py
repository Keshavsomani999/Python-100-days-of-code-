l = [11,45,1,2,4,6]
# print(l)
l.append(5) 
# l.sort()
# l.sort(reverse=True)

# print(l.index(1))   # 1 at which index

# print(l.count(11))

# m = l.copy()
# m[0] =0
# print(m)
# print(l)

# l.insert(1,22)
# print(l)

m = [900,1000,1100]
k = l+m
l.extend(m)
print(k)
