import sys

x1, y1, x2, y2 = map(int,sys.stdin.readline().split())

print(min(x1, y1, x2-x1, y2-y1))