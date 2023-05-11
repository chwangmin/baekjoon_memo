import sys

input = sys.stdin.readline

num = int(input())

list_num = list(map(int,input().rstrip()))

list_num2 = list(map(int,input().rstrip()))

tmp_list_num = list_num

tmp_list_num[0] = 0
tmp_list_num[1] = 0

i = 0
cnt = 0
while tmp_list_num != list_num2:
    if i == num-1:
        tmp_list_num[i - 1] = 0 if tmp_list_num[i - 1] else 1
        tmp_list_num[i] = 0 if tmp_list_num[i] else 1
        i = 0
    elif i == 0:
        tmp_list_num[i] = 0 if tmp_list_num[i] else 1
        tmp_list_num[i + 1] = 0 if tmp_list_num[i + 1] else 1
        i+=1
    else: 
        tmp_list_num[i - 1] = 0 if tmp_list_num[i - 1] else 1
        tmp_list_num[i] = 0 if tmp_list_num[i] else 1
        tmp_list_num[i + 1] = 0 if tmp_list_num[i + 1] else 1
        i+=1
    cnt +=1
    if cnt > num * 2:
        break

if cnt > num:
    print(num*2 - cnt)
else:
    print(cnt)