import sys

input = sys.stdin.readline

N = int(input())

razer_list = list(map(int,input().split()))

check_stack = []

answer_list = [0] * N

for i in range(N):
    while check_stack:
        if razer_list[check_stack[-1][0]] < razer_list[i]:
            check_stack.pop()
        else:
            answer_list[i] = check_stack[-1][0] + 1
            break
    check_stack.append((i,razer_list[i]))

print(*answer_list)
