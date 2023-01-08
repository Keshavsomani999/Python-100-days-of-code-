s1 = {1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2)) #Output :- {1, 2, 3, 5, 6, 7}

print(s1.intersection(s2)) #output :- {6}

print(s1.symmetric_difference(s2)) #output :- {1, 2, 3, 5, 7}

print(s1.difference(s2)) # {1, 2, 5}

print(s1.isdisjoint(s2)) # False

print(s1.issubset(s2)) # False