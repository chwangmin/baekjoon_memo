import sys

num = int(sys.stdin.readline())

for i in range(num):
    x, y = map(int,sys.stdin.readline().split())
    print(x+y)