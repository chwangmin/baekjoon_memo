# 이분 그래프 판별하기
# dfs로 판별
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
test_num = int(input())

isValied = True

def dfs(start):
    global isValied
    # 방문 했는지 확인(start)
    visited[start] = True
    # 1 부터 연결된 거 만큼 다 확인
    for i in adjacent[start]:
        # 방문하지 않았으면 방문
        if not visited[i]:
            # 팀의 i 의 값이 지금 부모의 값의 반대 값을 넣어줌 0 or 1
            team[i] = (team[start]+1)%2
            # dfs 한번 더 이동
            dfs(i)
        # 만약 부모와 자식이 같다면 False
        elif team[start] == team[i]:
            isValied = False

for _ in range(test_num):
    # 유효한지 확인
    isValied = True
    # 점 갯수와 선 갯수
    v,e = map(int ,input().split())
    # 방문했는지 초기 값을 False로
    visited = [False] * (v+1)
    # 어디랑 연결되어있는지 2차원으로 확인
    adjacent = [[]for _ in range(v+1)]
    # 0이 점 갯수개 만큼 있음
    team = [0] * (v+1) # T집합 또는 F집합
    # 선의 갯수 만큼 반복
    for _ in range(e):
        # p, q 로 연결상태 입력
        p ,q = map(int ,input().split())
        # p와 q 연결, q와 p 연결
        adjacent[p].append(q)
        adjacent[q].append(p)
    #점의 갯수 만큼 반복
    for i in range(1,v+1):
        # 유효 하다면 dfs(i)를 넣음
        # i 는 1의 점 부터 마지막 점까지
        if isValied:
            dfs(i)
        # 아니면 바로 멈춤 이미 팀이 겹쳐있는 경우가 있기 때문에.
        else:
            break
    if isValied:
        print("YES")
    else:
        print("NO")