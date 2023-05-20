import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

num = int(input())

num_list = list(map(int,input().split()))

answer_list = num_list[:]

budget = int(input())

avg_budget = budget // num

tmp_num = num

re = 1

while(re):
    re = 0
    for i in range(num):
        if num_list[i] == 0:
            continue
        if num_list[i] < avg_budget:
            budget -= num_list[i]
            num_list[i] = 0
            tmp_num -= 1
            re = 1

    if sum(num_list) < budget:
        answer = max(num_list)
        break
    else:
        avg_budget = budget // tmp_num
        answer = budget // tmp_num


if answer == 0:
    answer = max(answer_list)

print(answer)