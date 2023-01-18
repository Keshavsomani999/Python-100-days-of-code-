with open('myfile.txt','r') as f:
    print(type(f))

    f.seek(10)

    data = f.read()
    print(data)

#input
# Keshav is a good boy

# output
# a good boy

with open('sample.txt','w') as f:
    f.write("Hello world")
    f.truncate(5)

with open('sample.txt','r') as f:
    print(f.read())

# output
# Hello