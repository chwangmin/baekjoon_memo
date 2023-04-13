import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(1, num):
    j = i
    tmp = a[i]
    while j > 0 and a[j-1] > tmp:
        a[j] = a[j-1]
        j -= 1
    a[j] = tmp

print(a)