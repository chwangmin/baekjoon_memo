import sys

num = int(sys.stdin.readline())

col = list(map(int,sys.stdin.readline().split()))

all = []

def bf(arr, cur):
    if arr:
        for i in range(num-len(cur)):
            tmp = list(cur)
            tmp.append(arr[i])
            new_arr = arr[:i] + arr[i+1:]
            bf(new_arr,tmp)
    else:
        all.append(cur)

bf(col,[])

max_col = 0

for i in all:
    tmp = 0
    for j in range(num-1):
        tmp += abs(i[j] - i[j+1])
        if tmp > max_col:
            max_col = tmp

print(max_col)