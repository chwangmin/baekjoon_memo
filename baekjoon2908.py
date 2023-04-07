import sys

a, b = map(str,sys.stdin.readline().split())

c = [a[::-1],b[::-1]]

print(c)

print(max(c))
