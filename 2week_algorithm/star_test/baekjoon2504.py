import sys

input = sys.stdin.readline

bracket = list(input().rstrip())

tmp = 1
stack = []
answer = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        tmp *= 2
        stack.append(bracket[i])
    elif bracket[i] == '[':
        tmp *= 3
        stack.append(bracket[i])
    elif bracket[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif bracket[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif bracket[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)