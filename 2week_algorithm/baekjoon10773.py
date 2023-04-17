import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    su = int(input())

    if su == 0:
        stack.pop(-1)
    else:
        stack.append(su)

print(sum(stack))