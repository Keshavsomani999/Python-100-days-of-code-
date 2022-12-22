import time

Hours = int(time.strftime('%H'))

if(Hours<=12):
    print("Good Morning Sir")
elif(Hours<=17):
    print("Good Afternoon Sir")
elif(Hours<=18):
    print("Good Evening Sir")
else:
    print("Good night Sir")