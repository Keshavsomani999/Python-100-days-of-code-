# factorial(7*6*5*4*3*1)

#factorial(n) = n * factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# output :- 120

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

def fibonacci(n):
    if (n==0):
        return 0
    if (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=10

for i in range(n):
    print(fibonacci(i),end=" ")

# output :- 0 1 1 2 3 5 8 13 21 34 