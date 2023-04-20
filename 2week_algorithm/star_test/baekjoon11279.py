import sys
import heapq

input = sys.stdin.readline

num = int(input())

heap = []

for i in range(num):
    command = int(input())

    if command != 0:
        heapq.heappush(heap,-1 * command)
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)