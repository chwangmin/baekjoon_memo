import sys

input = sys.stdin.readline

num, k_need = map(int,input().split())

list_coin = []

for i in range(num):
    list_coin.append(int(input()))

answer = 0

for i in range(num-1,-1,-1):
    if k_need >= list_coin[i]:
        tmp = k_need // list_coin[i]
        k_need -= list_coin[i] * tmp
        answer += tmp
    if k_need == 0:
        break

print(answer)