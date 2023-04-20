import sys
import heapq

input = sys.stdin.readline

num = int(input())

heap = []

for _ in range(num):
    heapq.heappush(heap,int(input()))

answer = 0

if num == 1:
    print(heap[0])
else:
    for _ in range(num):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        check = x + y
        answer += check
        if not heap:
            break
        heapq.heappush(heap,check)

    print(answer)
