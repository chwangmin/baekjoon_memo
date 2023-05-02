import sys

input = sys.stdin.readline

num_con, num_ele = map(int,input().split())

list_tmp = [0] * (num_ele + 1)

list_num = list(map(int,input().split()))

for i in list_num:
    list_tmp[i] += 1

list_tmp.sort(reverse=True)

answer = 0

for i in range(num_con, num_ele+1):
    answer += list_tmp[i]

print(answer)