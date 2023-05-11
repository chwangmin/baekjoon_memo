import sys

input = sys.stdin.readline

num = int(input())

list_num = list(map(int,input().split()))

answer = 0

i = 1

for _ in range(1,num):
    if i >= num:
        break
    if i == num - 1:
        answer += abs(list_num[i]-list_num[i-1])
        i += 1
        continue
    if abs(list_num[i+1]-list_num[i]) < abs(list_num[i]-list_num[i-1]):
        answer += abs(list_num[i]-list_num[i-1])
        i += 2
    elif list_num[i-1] < list_num[i] < list_num[i+1]:
        cnt = 0
        for j in range(i+2, num):
            if list_num[j] > list_num[j-1]:
                cnt +=1
            else:
                break
        answer += list_num[i+1+cnt] - list_num[i-1]
        i += 3 + cnt
    elif list_num[i-1] > list_num[i] > list_num[i+1]:
        cnt = 0
        for j in range(i+2, num):
            if list_num[j] < list_num[j-1]:
                cnt +=1
            else:
                break
        answer += list_num[i-1] - list_num[i+1+cnt]
        i += 3+cnt
    else:
        answer += abs(list_num[i+1] - list_num[i])
        i += 3

print(answer)