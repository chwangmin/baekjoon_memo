import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    count = 0
    stack = input().strip()
    for i in stack:
        if i == "(":
            count -= 1
        else:
            count += 1
        if count > 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")