import sys

input = sys.stdin.readline

num = int(input())

d = [0] * (num + 1)

d[1] = 1
d[2] = 2

for i in range(3, num + 1):
    d[i] = d[i-2] + d[i-1]
    d[i] %= 15746

print(d[num])