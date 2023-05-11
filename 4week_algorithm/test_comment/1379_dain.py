# 내 코드 아닙니다.
from heapq import heappush, heappop
from collections import deque
from sys import stdin as s

n = int(s.readline().strip())

table_num = [[0] for _ in range(n+1)]

time_table = [list(map(int, s.readline().split())) for _ in range(n)]

time_table.sort(key = lambda x: (x[1], x[2]))

heap = []
# empty_room = heapq()
empty_room = []
# for i in range(n, 0, -1):
#     # empty_room.append(i)
#     heappush(empty_room, i)
#     print(empty_room)

for i in range(1, n+1):
    # empty_room.append(i)
    heappush(empty_room, i)
    print(empty_room)

# 입력 값들.
for i in time_table:
    # 타임 테이블에 있던 num, start, end 값 ex) 6 15 21
    num, start, end = i

    # 맨처음에 오는게 가장 빨리 끝나는 강의
    while heap and heap[0][0] <= start:
        # 반복문의 i보다 먼저 끝나면 그 강의를 빼서 리뉴얼시켜 넣어줌
        # 가장 빨리 끝나는 강의
        end1, empty1 = heappop(heap)
        # empty_room.append(empty1)
        # 빈강의실에 넣어줌
        heappush(empty_room, empty1)

    # empty_room에 가장 작은 값을 empty로 빼줍니다.
    empty = heappop(empty_room)
    # 마지막 값부터 end 까지 빼줍니다.
    # 처음으로 heappush를 해서 다음 부터는 heap을 사용해서 무한 루프
    heappush(heap, [end, empty])
    table_num[num] = empty

table_num = table_num[1:]
print(max(table_num))
for i in table_num:
    print(i)