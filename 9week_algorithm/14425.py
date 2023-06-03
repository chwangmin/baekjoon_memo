import sys

input = sys.stdin.readline

n, m = map(int,input().split())

S_list = set()

for i in range(n):
    S_list.add(input())

answer = 0

for i in range(m):
    S_input = input()
    if S_input in S_list:
        answer+=1

print(answer)
