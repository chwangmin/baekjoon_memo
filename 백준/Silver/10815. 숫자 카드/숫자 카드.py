import sys

input = sys.stdin.readline

numSang = int(input())

listSang = list(map(int,input().split()))

numCheck = int(input())

listCheck = list(map(int,input().split()))

_dict = {}
for i in range(numSang):
    _dict[listSang[i]] = 0

for j in range(numCheck):
    if listCheck[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')