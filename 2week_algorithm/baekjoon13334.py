import sys
import heapq

n = int(sys.stdin.readline())
# road info에 모든 road를 넣음
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

# 지정한 길이 를 d로 정의
d = int(sys.stdin.readline())
roads = []

# 저장된 road_info 값안에서 for문을 돌림.
for road in road_info:
    house, office = road
    # 만약에 길이가 선택한 d 길이보다 작으면 정렬하고 roads.에 넣음
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
# roads의 값들을 마지막 x좌표를 통해 정렬
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    # heap이 없다면 road 값 push
    if not heap:
        heapq.heappush(heap, road)
    else:
        # 아니면 heap 첫번째(Min)의 시작 지점이 이 마지막 x좌표 - 선택한 길이(d) 보다 작다면
        while heap[0][0] < road[1] - d:
            # heap의 가장 작은 값이 포함이 안된다는 뜻이라 가장 위의 값 pop 
            # 다시 heapq 정렬한 후 다시 pop
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)