Question = ["Which animal is known as the 'Ship of the Desert'?","How many letters are there in the English alphabet?","Rainbow consist of how many colours?"]
Ans = ["Camel","26","7"]

print("Welcome To KBC ")
Total_Win = 0
print("Total Win =",Total_Win)


for i in range(len(Question)):
    print(Question[i])
    user_ans = input()
    print("Your Answere : ",user_ans)
    if(user_ans==Ans[i]):
        print("Correct Answere")
        Total_Win += 1000
        print("Total Win =",Total_Win)
    else:
        print("Wrong Answere")
        print("Total Win =",Total_Win)
