import sys

input = sys.stdin.readline

n, k = map(int,input().split())

baby_list = list(map(int,input().split()))

difference_list = []

for i in range(n-1):
    difference_list.append(baby_list[i+1]-baby_list[i])

difference_list.sort()

for i in range(k-1):
    difference_list.pop()

print(sum(difference_list))