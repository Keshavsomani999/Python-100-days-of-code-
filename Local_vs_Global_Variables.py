x =4
print(x)

def hello():
    global x
    
    x = 5
    print(f"The local x is {x}")

hello()

print(f"The global variable is {x}")