import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int,input().split()))

list_check = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and list_check[i] < list_check[j]:
            list_check[i] = list_check[j]
    list_check[i] += 1

print(max(list_check))

