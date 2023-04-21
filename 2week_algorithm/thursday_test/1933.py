# 내가 짠거 아님.

import heapq
import sys
N = int(input())
buildings = []
end_points = []

for i in range(N):
    start, height, end = map(int,input.split())

    buildings.append((i,start,height,0))
    buildings.append((i,end,height,1))

    end_points((end))

buildings.sort(key=lambda x: (x[1],x[3],-x[2]))

current_height = 0
end_list = set()
result = []
not_ended_building = []

for building in buildings:
    building_idx, x, height, is_end = building

    if not is_end:
        if height > current_height:
            current_height = height
            result.append((x,current_height))

        heapq.heappush(not_ended_building,(-height,end_points[building_idx]))
        continue

    end_list.add(x)

    while not_ended_building and not_ended_building[0][1] in end_list:
        heapq.heappop(not_ended_building)

    if not_ended_building:
        if current_height != -not_ended_building[0][0]:
            current_height = -not_ended_building[0][0]
            result.append((x,current_height))

    else:
        if current_height != 0:
            current_height = 0
            result.append((x,current_height))
for r in result:
    print(' '.join([str(r[0]), str(r[1])]),end = ' ')