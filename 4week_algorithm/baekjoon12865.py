import sys

sys.stdin = open('./input.txt', 'rt')

input = sys.stdin.readline

num, k_limit = map(int,input().split())

list_bag = []

for i in range(num):
    tmp_bag = list(map(int,input().split()))
    if tmp_bag[0] > k_limit:
        continue
    list_bag.append(tmp_bag)

max_size = - sys.maxsize

for i in range(num):
    tmp_k_limit = k_limit
    tmp_max_size = 0
    visited = [0] * num
    if tmp_k_limit >= list_bag[i][0]:
        tmp_k_limit -= list_bag[i][0]
        tmp_max_size = list_bag[i][1]
        visited[i] = 1
    for j in range(num):
        if tmp_k_limit == 0:
            break
        if tmp_k_limit >= list_bag[j][0] and not visited[j]:
            tmp_k_limit -= list_bag[j][0]
            tmp_max_size += list_bag[j][1]
            visited[j] = 1
    max_size = max(tmp_max_size,max_size)
    
print(max_size)