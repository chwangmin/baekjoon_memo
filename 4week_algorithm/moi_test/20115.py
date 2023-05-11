import sys

input = sys.stdin.readline

num = int(input())

list_num = list(map(int,input().split()))

answer_tmp = max(list_num)
answer = 0

for i in list_num:
    if answer_tmp == i:
        continue
    answer += i / 2

print(answer_tmp + answer)
    