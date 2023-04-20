import sys

input = sys.stdin.readline

brackets = input().rstrip()

tmp = 1
answer = 0
stack = []

for i in range(len(brackets)):
    if brackets[i] == '(':
        tmp *= 2
        stack.append(brackets[i])
    elif brackets[i] == '[':
        tmp *= 3
        stack.append(brackets[i])
    elif brackets[i] == ')':
        if stack and stack[-1] == '[':
            answer = 0
            break
        if brackets[i-1] == '(':
            answer += tmp
        if not stack:
            answer = 0
            break
        stack.pop()
        tmp //= 2
    else :
        if stack and stack[-1] == '(':
            answer = 0
            break
        if brackets[i-1] == '[':
            answer += tmp
        if not stack:
            answer = 0
            break
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)

