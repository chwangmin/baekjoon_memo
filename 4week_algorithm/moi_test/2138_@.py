import sys

input = sys.stdin.readline

def first_check():
    cnt = 1
    list_tmp = list_num1[:]
    list_tmp[0] = 0 if list_tmp[0] else 1
    list_tmp[1] = 0 if list_tmp[1] else 1
    for i in range(1,num):
        if list_tmp[i-1] != list_num2[i-1]:
            cnt +=1
            list_tmp[i-1] = 0 if list_tmp[i-1] else 1
            list_tmp[i] = 0 if list_tmp[i] else 1
            if i < num - 1:
                list_tmp[i+1] = 0 if list_tmp[i+1] else 1
    if list_tmp == list_num2:
        return cnt
    return 100002

def no_first_check():
    cnt = 0
    list_tmp = list_num1[:]
    for i in range(1,num):
        if list_tmp[i-1] != list_num2[i-1]:
            cnt +=1
            list_tmp[i-1] = 0 if list_tmp[i-1] else 1
            list_tmp[i] = 0 if list_tmp[i] else 1
            if i < num - 1:            
                list_tmp[i+1] = 0 if list_tmp[i+1] else 1
    if list_tmp == list_num2:
        return cnt
    return 100002

num = int(input())

list_num1 = list(map(int,input().rstrip()))

list_num2 = list(map(int,input().rstrip()))

cnt_fc = first_check()
cnt_nfc = no_first_check()

answer = min(cnt_fc, cnt_nfc)
if answer == 100002:
    print(-1)
else:
    print(answer)