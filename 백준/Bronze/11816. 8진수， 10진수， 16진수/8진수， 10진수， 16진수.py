import sys

input = sys.stdin.readline

num = input().rstrip()

if num[0] == "0":
    if num[1] == "x":
        print(int(num,16))
    else:
        print(int(num,8))
else:
    print(num)