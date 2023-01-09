dic = {
    "Keshav":"Human Being",
    "spoon":"Object"
}

print(dic['Keshav'])

print(dic.keys())
print(dic.values()) 

for key,value in dic.items():
    print(f"the value corresponding to the key {key} is {value}")