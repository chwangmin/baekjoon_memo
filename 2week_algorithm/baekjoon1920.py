import sys

num1 = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

num2 = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

a.sort()

def binary_search(x, left, right):
    mid = (left + right) // 2 - 1
    if x == a[mid]:
        return True
    if left < right:
        if x > a[mid]:
            binary_search(x,mid+1,right)
        else:
            binary_search(x,left,mid-1)



for i in b:
    if binary_search(i,0,num1):
        print(1)
    else:
        print(0)
