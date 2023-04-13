import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(num):
    min = i
    for j in range(i+1,num):
        if a[j] < a[min]:
            min = j
    a[i], a[min] = a[min], a[i] 

print(a)