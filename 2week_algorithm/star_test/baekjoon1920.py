from sys import stdin

input = stdin.readline

N = int(input())

A = list(map(int,input().split()))

A.sort()

M = int(input())

M_list = list(map(int,input().split()))

for i in M_list:
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right) // 2
        if A[mid] <= i:
            left = mid + 1
        else:
            right = mid - 1
    if A[right] == i:
        print(1)
    else:
        print(0)
