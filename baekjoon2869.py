import sys

A, B, V = map(int,sys.stdin.readline().split())

X = (V-A)/(A-B)

if X-int(X) > 0:
    print(int(X) + 2)
else:
    print(int(X) + 1)