import sys

input = sys.stdin.readline

def dfs(first_person, second_person, cnt):
    if first_person == second_person:
        print(cnt)
        exit()
    visited[first_person] = 1
    for i in graph_relation[first_person]:
        if not visited[i]:
            dfs(i, second_person, cnt+1)


people_num = int(input())

first_person, second_person = map(int,input().split())

relation_edges = int(input())

graph_relation = [[] for _ in range(people_num+1)]

visited = [0] * (people_num + 1)

for _ in range(relation_edges):
    parent, child = map(int,input().split())

    graph_relation[parent].append(child)
    graph_relation[child].append(parent)

x = dfs(first_person,second_person,0)
if x:
    print(x)
else:
    print(-1)

