import sys

num = int(sys.stdin.readline())

def factorial(num):
    x = 1
    if num > 1:
        x = num * factorial(num-1)
    return x

if num < 2:
    print(1)
else:
    print(factorial(num))
