import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())

q = deque([])

answer = []

for i in range(1,N+1):
    q.append(i)

q.reverse()

while q:
    for i in range(K-1):
        q.rotate()
    answer.append(q[-1])
    q.pop()

print('<', end='')
print(*answer, sep=', ', end ='')
print('>')
