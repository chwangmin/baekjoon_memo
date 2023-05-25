import sys

input = sys.stdin.readline

n, m = map(int,input().split())

num_list = list(map(int,input().split()))

num_list.sort()

for i in range(m):
    tmp = num_list[0] + num_list[1]
    num_list[0] = tmp
    num_list[1] = tmp
    num_list.sort()

print(sum(num_list))