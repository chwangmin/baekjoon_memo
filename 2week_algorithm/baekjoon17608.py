import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    stack.append(int(input()))

very_big = stack[-1]
count = 1

for i in range(N):
    if stack[-1] > very_big:
        very_big = stack[-1]
        count+=1
    stack.pop()

print(count)