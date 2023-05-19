import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

list_map = []

n = int(input())
m = int(input())

answer_list = [float('inf')] * (n+1)

for i in range(m):
    x,y,z = map(int,input().split())
    list_map.append((x,y,z))

list_map.sort(key = lambda x: (x[0]))

for list in list_map:
    if list[0] == 1:
        answer_list[list[1]] = list[2]
        continue
    

start, end = map(int,input().split())