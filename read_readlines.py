# f = open('myfile.txt','r')
# while True:
#     line = f.readline()
   
#     if not line:
#         break
#     print(line)

# output
# Keshav somani is a great man

# and this toutorail is also awesome \

# this is good

# f = open('myfile.txt','r')
# i=0 
# while True:
#     i = i+1
#     line = f.readline()

#     if not line:
#         break
#     m2 = int(line.split(",")[1])
#     m1 = int(line.split(",")[0])
#     m3 = int(line.split(",")[2])
#     print(f"marks of student {i} in maths is : {m1*2}")
#     print(f"marks of student {i} in English is : {m2}")
#     print(f"marks of student {i} in SST is : {m3}")
    
#output
# marks of student 1 in maths is : 112
# marks of student 1 in English is : 45
# marks of student 1 in SST is : 67
# marks of student 2 in maths is : 24
# marks of student 2 in English is : 34
# marks of student 2 in SST is : 63
# marks of student 3 in maths is : 26
# marks of student 3 in English is : 64
# marks of student 3 in SST is : 23

f = open('myfile2.txt','w')

lines = ['line 1\n','line 2\n','line 3\n']

for line in lines:
    f.write(line +'\n')
# f.writelines(lines)
f.close()