import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())

q = deque([])

for i in range(1, N+1):
    q.append(i)

q.reverse()

while len(q) > 1:
    q.pop()
    q.rotate()

print(*q)

