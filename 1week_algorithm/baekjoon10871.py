import sys

n, x = map(int,sys.stdin.readline().split())

y = list(map(int,sys.stdin.readline().split()))

for i in y:
    if i < x:
        print(i, end=' ')
