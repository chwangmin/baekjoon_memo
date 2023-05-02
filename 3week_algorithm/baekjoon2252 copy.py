import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

# 위상 정렬을 위한 어디와 연결되어 있는지 확인하는 리스트
graph = [[] for _ in range(n+1)]
# inDegree 0으로 초기화
inDegree = [0 for _ in range(n+1)]
# 큐 설정
queue = deque()
# 정답 리스트
answer = []

#m 만큼 반복
for i in range(m):
    #a, b 값 들어오기
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # 그래프 a 에 b 값 추가
    graph[a].append(b)
    # 진입 차수 추가하기
    inDegree[b] += 1

# 1 부터 n + 1까지
for i in range(1, n+1):
    # 진입차수가 0인 것들을 큐에 넣음.
    if inDegree[i] == 0:
        queue.append(i)

# 큐에 무한 반복
while queue:
    # tmp 에 큐 값 팝해서 넣음 나중에 넣은 것을 첫번째로
    tmp = queue.popleft()
    # 정답 값에 tmp 추가
    answer.append(tmp)
    # tmp에 이어진 것을 i 값으로 받아옴
    for i in graph[tmp]:
        # 진입 차수를 하나 삭제함
        # 연결 되어 있는 간선이 하나 없어졌기 때문이다.
        inDegree[i] -= 1
        # 간선이 0 이라면
        if inDegree[i] == 0:
            # 큐에 i 추가
            queue.append(i)

# answer 값 출력.
print(*answer)