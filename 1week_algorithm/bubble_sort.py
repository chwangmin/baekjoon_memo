import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(num):
    for j in range(num-1,i,-1):
        if a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]

print(a)