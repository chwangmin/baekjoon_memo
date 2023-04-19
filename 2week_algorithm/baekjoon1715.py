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
    for i in range(N):
        count +=1
        if count > 2:
            x = answer
            answer += x
            count = 1
        answer += heapq.heappop(heap)

    print(answer)

    
