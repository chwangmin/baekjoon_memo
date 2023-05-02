import sys
from sys import maxsize
import heapq

input = sys.stdin.readline

def dijkstra(start_city):
    pq = []
    heapq.heappush(pq,(0,start_city))
    distance[start_city]= 0

    while pq:
        d, x = heapq.heappop(pq)

        if distance[x] < d:
            continue
        for nw, nx in matrix[x]:
            nd = d + nw
            if distance[nx] > nd:
                heapq.heappush(pq,(nd,nx))
                distance[nx] = nd

num_city = int(input())

num_bus = int(input())

distance = [0] + [maxsize] * (num_city)