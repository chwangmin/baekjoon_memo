import sys
import heapq

input = sys.stdin.readline

num = int(input())

leftheap = []
rightheap = []

for i in range(num):
    x = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,-1 * x)
    else:
        heapq.heappush(rightheap,x)
    if rightheap and -1 * leftheap[0] > rightheap[0]:
        tmp = heapq.heappop(rightheap)
        heapq.heappush(rightheap,-1 * heapq.heappop(leftheap))
        heapq.heappush(leftheap,-1 * tmp)
    print(-1 * leftheap[0])