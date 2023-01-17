
# Reading a file
# f = open('myfile.txt','r')
# txt = f.read()
# print(txt)
# f.close()

#write a file

# f = open('myfile.txt','a')
# f.write('hello world')
# f.close()

# you not want add close 
with open('myfile.txt','a') as f:
    f.write("i am inside with")