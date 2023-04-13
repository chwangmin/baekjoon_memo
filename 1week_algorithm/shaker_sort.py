import sys

num = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

left = 0
right = num-1
last = right

while left < right:
    for j in range(right,left,-1):
        if a[j-1] > a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            last = j
    left = last
    for j in range(left,right):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            last = j
    right = last

print(a)