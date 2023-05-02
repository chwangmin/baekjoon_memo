import sys
from sys import maxsize
import heapq

input = sys.stdin.readline

def dijkstra(start_city):
    pq = []
    heapq.heappush(pq, (0, start_city))
    distance[start_city] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if distance[x] < d:
            continue

        for nw, nx in matrix[x]:
            # 총 거리
            nd = d + nw

            # 총거리가 distance 에 저장되어 있는 값보다 작으면 heapq.heappush
            if distance[nx] > nd:
                heapq.heappush(pq, (nd,nx))
                distance[nx] = nd


num_city = int(input())

num_bus = int(input())

distance = [0] + [maxsize] * (num_city)

matrix = [[] for _ in range(num_city + 1)]

for _ in range(num_bus):
    bus_start_city, bus_end_city, cost_bus = map(int,input().split())
    matrix[bus_start_city].append((cost_bus, bus_end_city))

start_city, end_city = map(int,input().split())

distance[start_city] = 0

dijkstra(start_city)

print(distance[end_city])

