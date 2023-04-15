import sys

input = sys.stdin.readline

num = int(input())

bag = 0

while num >= 0:
    if num % 5 == 0:
        bag = bag + num//5
        break
    num -= 3
    bag += 1
if num < 0:
    print(-1)
else:
    print(bag)