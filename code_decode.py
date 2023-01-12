import random
import string

def code():
    inp = list(input("Enter the string to code : - ").split(" "))
    for i in range(0,len(inp)):
        if(len(inp[i])<3):
            inp1 = inp[i]
            print (inp1[::-1],end=" ")
        else:
            inp1 = inp[i]
            la = inp[i][0]
            inp2 = inp[i][1:]
            inp3 = inp2+la
            start= ""
            last=""
            for i in range(0,3):
                start=start+(random.choice(string.ascii_letters))
            for i in range(0,3):
                last=last+(random.choice(string.ascii_letters))

            print(start+inp3+last,end=" ")


def decode():
    inp = list(input("Enter the string to code : - ").split(" "))
    for i in range(0,len(inp)):
        if(len(inp[i])<3):
            inp1 = inp[i]
            print (inp1[::-1],end=" ")
        else:
            
            inp1=inp[i][3:len(inp[i])-3]
            inp2 = inp1[len(inp1)-1:]
            inp3 = inp1[:len(inp1)-1]
            print(inp2+inp3,end=)

ques = int(input("Press 1 : code \n      2 : Decode  "))

if(ques == 1):
    code()
elif(ques==2):
    decode()
else:
    print("Wrong input , Please enter 1 or 2")
