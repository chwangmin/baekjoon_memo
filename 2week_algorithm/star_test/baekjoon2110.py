from sys import stdin

input = stdin.readline

house_num, router_num = map(int,input().split())

list_house = []

for i in range(house_num):
    list_house.append(int(input()))

list_house.sort()

left = 1
right = list_house[-1] - list_house[0]

while left <= right:
    cnt = 1
    mid = (left+right) // 2
    val = list_house[0]

    for i in range(1, house_num):
        if list_house[i] >= mid + val:
            cnt += 1
            val = list_house[i]
    if cnt >= router_num:
        left = mid + 1
    else:
        right = mid - 1

print(right)