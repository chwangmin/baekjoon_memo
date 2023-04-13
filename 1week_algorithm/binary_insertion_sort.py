import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(1,num):
    key = a[i]
    pl = 0
    pr = i - 1

    while True:
        pc = (pl+pr) // 2
        if a[pc] == key:
            break
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break

    pd = pc + 1 if pl <= pr else pr + 1

    for j in range(i, pd, -1):
        a[j] = a[j-1]
    a[pd] = key

print(a)