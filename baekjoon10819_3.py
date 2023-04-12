import sys

num = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split()))

all = []

def bf(arr,cur):
    global count
    if arr:
        for i in range(num-len(cur)):
            tmp = list(cur)
            tmp.append(arr[i])
            new_arr = list(arr[:i] + arr[i+1:])
            bf(new_arr,tmp)
    else:
        all.append(cur)

max = 0

bf(x,[])

for i in all:
    tmp = 0
    for j in range(num-1):
        tmp += abs(i[j] - i[j+1])
    if max < tmp:
        max = tmp

print(max)
