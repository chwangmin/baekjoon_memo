import sys

input = sys.stdin.readline

stick_list = list(input().rstrip())

tmp_count = 0
answer = 0
for i in range(len(stick_list)):
    if stick_list[i] == ')':
        if stick_list[i-1] == '(':
            answer += tmp_count
        else:
            answer += 1
            tmp_count -= 1
    else:
        if stick_list[i+1] == ')':
            continue
        tmp_count += 1

print(answer)