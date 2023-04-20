import sys
import heapq

input = sys.stdin.readline

N = int(input())

x = 0

answer = 0

heap = []

for i in range(N):
    inputNum = int(input())

    heapq.heappush(heap,inputNum)

count = 0

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        plus = heapq.heappop(heap) + heapq.heappop(heap)
        answer += plus
        heapq.heappush(heap,plus)

    print(answer)

    
