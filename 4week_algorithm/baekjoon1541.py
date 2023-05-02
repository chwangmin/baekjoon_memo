import sys

input = sys.stdin.readline

minus_split = input().split('-')

check_nums = []

for i in minus_split:
    list_tmp = i.split('+')
    tmp = 0
    for j in list_tmp:
        tmp += int(j)
    check_nums.append(tmp)

answer = check_nums[0]

for i in range(1,len(check_nums)):
    answer -= check_nums[i]

print(answer)

    