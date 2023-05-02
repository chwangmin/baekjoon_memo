import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_city):
    que = deque()
    que.append(start_city)
    while que:
        start_city = que.popleft()
        for i in matrix[start_city]:
            if distance[i[0]] > distance[start_city] + i[1]:
                distance[i[0]] = distance[start_city] + i[1]
            que.append(i[0])

num_city = int(input())

num_bus = int(input())

distance = [0] + [100001] * (num_city)

matrix = [[] for _ in range(num_city + 1)]

for _ in range(num_bus):
    bus_start_city, bus_end_city, cost_bus = map(int,input().split())
    matrix[bus_start_city].append((bus_end_city,cost_bus))

start_city, end_city = map(int,input().split())

distance[start_city] = 0

bfs(start_city)

print(distance[end_city])

