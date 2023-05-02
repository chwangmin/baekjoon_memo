import sys

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    tmp_num = []
    num_people = int(input())
    for _ in range(num_people):
        x, y = map(int,input().split())
        if x == 1:
            check_y = y
        if y == 1:
            check_x = x
        tmp_num.append((x,y))
    for i in tmp_num:
        if i[0] > check_x:
            num_people -= 1
        elif i[1] > check_y:
            num_people -= 1
    print(num_people)