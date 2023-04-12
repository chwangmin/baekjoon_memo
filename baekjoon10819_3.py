import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

all = []

def bf(arr,cur):
    if arr:
        for i in range(num-len(cur)):
            tmp = list(cur)
            tmp.append(arr[i])
            new_arr = arr[:i] + arr[i+1:]
            bf(new_arr,tmp)
    else:
        all.append(cur)

bf(a, [])

check = 0

for i_list in all:
    tmp = 0
    for i in range(num-1):
        tmp += abs(i_list[i] - i_list[i+1])
    if check < tmp:
        check = tmp

print(check)
