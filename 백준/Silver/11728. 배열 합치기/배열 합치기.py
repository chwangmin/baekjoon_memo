import sys

input = sys.stdin.readline

input()

a = list(map(int,input().split()))

b = list(map(int,input().split()))

c = a + b

print(*sorted(c), sep=" ")