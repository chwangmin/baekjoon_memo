import sys, itertools, collections

input = sys.stdin.readline

def bfs(same):
    start = same[0]
    queue = collections.deque([start])
    visited = set([start])
    _sum = 0
    while queue:
        v = queue.pop()
        _sum += people_num_list[v]
        for u in graph_list[v]:
            if u not in visited and u in same:
                queue.append(u)
                visited.add(u)
    return _sum, len(visited)

num = int(input().strip())
people_num_list = [int(x) for x in input().split()]
graph_list = collections.defaultdict(list)
answer = float('inf')

for i in range(num):
    tmp_list = [int(x) for x in input().split()]
    for j in range(1, tmp_list[0]+1):
        graph_list[i].append(tmp_list[j]-1)

for i in range(1, num//2 + 1):
    combis = itertools.combinations(range(num),i)
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(num) if i not in combi])
        if v1 + v2 == num:
            answer = min(answer, abs(sum1 - sum2))

if answer != float('inf'):
    print(answer)
else:
    print(-1)