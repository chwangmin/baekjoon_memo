import sys

input = sys.stdin.readline

N, count = map(int,input().split())

num_list = input().rstrip()

stack = []

for i in num_list:
    while stack and stack[-1] < int(i) and count > 0:
        stack.pop()
        count -= 1
    stack.append(int(i))
while stack and count > 0:
    stack.pop()
    count -= 1

print(*stack, sep='')