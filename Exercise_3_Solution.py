questions = [
    ["which language was used to create fb?","python","French","JavaScript","php","None",4
],

   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],

   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
   ["which language was used to create fb?","python","French","JavaScript","php","None",4
],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
i= 0

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a.{question[1]}              b.{question[2]}")
    print(f"a.{question[3]}              b.{question[4]}")

    replay = int(input("Enter your answere (1-4) "))

    if (replay == question[-1]):
        print(f"correct answere, you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money == 10000000
    else:
        print("Wrong answer !")
        break

print(f"Your take home money is {money}")