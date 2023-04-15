import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [0] * (n + 1)
d[0] = 1


for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))

