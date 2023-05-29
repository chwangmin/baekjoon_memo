import sys, itertools, collections

def bfs(same):
    start = same[0] # 처음 시작을 0으로 설정
    q = collections.deque([start]) # deque를 start로 지정
    visited = set([start]) # start를 방문했다고 지정
    _sum = 0 # 총 합을 0으로 초기값 지정
    while q: # q가 비어있지 않을 때 까지.
        v = q.popleft() # v를 q의 pop 한걸 넣는다 처음에는 start
        _sum += pp[v] # v의 인구수 추가
        for u in g[v]: # g[v] v와 연결되어 있는 것들을 모두 돌아봄
            if u not in visited and u in same: # u가 방문하지 않고 u 가 same에 있다면
                q.append(u) # q에 u를 넣는다.
                visited.add(u) # 방문에 u를 넣는다.
    return _sum, len(visited) # q가 모두 확인되면 _sum과 방문한 길이를 리턴해준다.

n = int(sys.stdin.readline().strip()) # 몇 개 할 것인지 숫자 입력
pp = [int(x) for x in sys.stdin.readline().split()] # 그 다음 인구의 수를 입력
g = collections.defaultdict(list) # list로 몇번째에 뭐가 있는지 초기값 추가.
result = float('inf') # result를 inf로 설정 초기

for i in range(n): # n 번 반복
    _input = [int(x) for x in sys.stdin.readline().split()] # 숫자들 _input으로 입력
    for j in range(1, _input[0]+1): # 1 ~ 부터 입력
        g[i].append(_input[j]-1) # g[i] 0번째부터 입력하는데 -1을 해줌.

for i in range(1, n//2 + 1): # 1 ~ n//2+1 만큼해도 모든 경우의 수를 찾을 수 있음
    combis = list(itertools.combinations(range(n), i)) # 1일때 경우의 수 그룹 ~ n//2 + 1 그룹의 수 만큼 찾기 
    for combi in combis: # 경우의 수 combi를 찾기
        sum1, v1 = bfs(combi) # 첫번째 경우의 총 인구 수와 길이 측정
        sum2, v2 = bfs([i for i in range(n) if i not in combi]) # 두번째 경우의 총 인구 수와 길이 측정
        if v1 + v2 == n: #2번의 bfs를 통해 모든 노드가 방문되었는지 확인한다.
            result = min(result, abs(sum1 - sum2)) # 합의 차이를 최솟값으로 지정

if result != float('inf'): # 결과가 무한이 아니면 연결 성공한 것이 하나라도 있으니
    print(result) # result를 출력
else: # 아니면
    print(-1) # -1을 출력