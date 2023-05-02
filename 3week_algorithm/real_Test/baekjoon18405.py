from collections import deque
# 상, 하, 좌, 우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, k = map(int, input().split())
# 전체 보드 정보와 바이러스 정보를 담는 리스트
board = []
virus = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    # 해당 위치에 바이러스가 있다면, virus 리스트에 추가
    for j in range(n):
        if row[j] != 0:
            virus.append((row[j], 0, i, j))
# 바이러스 순서대로 정렬
virus.sort()
# S초, X좌표, Y좌표
s, x, y = map(int, input().split())
# BFS 수행
q = deque(virus)
while q:
    v, t, now_x, now_y = q.popleft()
    # S초가 지난 경우
    if t == s:
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        # 범위를 벗어나는 경우 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 이미 바이러스가 있는 경우 무시
        if board[nx][ny] != 0:
            continue
        # 새로운 바이러스 추가
        board[nx][ny] = v
        q.append((v, t+1, nx, ny))
print(board[x-1][y-1])