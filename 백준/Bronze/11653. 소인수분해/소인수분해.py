import sys

#sys.stdin = open("test.txt",'r')

input = sys.stdin.readline

num = int(input())

i = 2

while True:
    if num == 1:
        break
    if num % i == 0:
        print(i)
        num = num // i
        i = 2
        continue
    i += 1