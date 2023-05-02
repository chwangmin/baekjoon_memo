import sys

input = sys.stdin.readline

d = [0] * 10000001

d[1] = 1
d[2] = 2

num = int(input())

for i in range(3,num+1):
    d[i] = (d[i-2] + d[i-1]) % 15746

print(d[num])