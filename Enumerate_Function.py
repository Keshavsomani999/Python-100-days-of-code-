marks =[12,56,32,98,12,45,1,4]

# Method 1
# index =0
# for mark in marks:
#     print(mark)
#     if(index ==3):
#         print("Keshav","awesome!")
    
#     index +=1


# Method 2 Enumerate Function
index =0
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index ==3):
        print("Keshav","awesome!")

