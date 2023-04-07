import sys

num = int(sys.stdin.readline())

x = 1
def factorial(num):
    if num > 1:
        global x
        x *= num    
        factorial(num-1)
    return x

if num < 2:
    print(1)
else:
    print(factorial(num))
