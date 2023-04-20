import sys

input = sys.stdin.readline

num = int(input())

list_top = list(map(int,input().split()))

stack = []
answer = [0] * num

for i in range(num):
    if not stack:
        stack.append((i,list_top[i]))
    else:
        if stack[-1][1] < list_top[i]:
            while stack and stack[-1][1] < list_top[i]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][0] + 1
            stack.append((i,list_top[i]))
        else:
            answer[i] = stack[-1][0] + 1
            stack.append((i,list_top[i]))

print(*answer)