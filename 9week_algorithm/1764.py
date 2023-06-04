import sys

input = sys.stdin.readline

n, m = map(int,input().split())

d_list = set()

for i in range(n):
    d_list.add(input().rstrip())

b_list = set()
for i in range(m):
    b_list.add(input().rstrip())

answer = sorted(list(d_list & b_list))

print(len(answer))
for i in answer:
    print(i)