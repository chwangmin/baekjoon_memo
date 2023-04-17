import sys

input = sys.stdin.readline

N = int(input())

heap = [0]

# insert
def insert(heap, num):
    heap.append(num)

    i = len(heap) - 1
    while i > 1:
        if heap[i] < heap[i//2]:
            tmp = heap[i]
            heap[i] = heap[i//2]
            heap[i//2] = tmp
            i = i // 2
        else:
            break

for i in range(N):
    insert(heap,int(input()))
    print(heap)