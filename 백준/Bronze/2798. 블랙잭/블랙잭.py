import sys

input = sys.stdin.readline

num, sumCard = map(int,input().split())

listCard = list(map(int,input().split()))

result = 0

for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1,num):
            if sumCard < listCard[i] + listCard[j] + listCard[k]:
                continue
            else:
                result = max(result, listCard[i] + listCard[j] + listCard[k])

print(result)