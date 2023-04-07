import sys

## input() 대신 sys.stdin.readline() 을 쓰면 빠르다.
a, b = map(int,sys.stdin.readline().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)