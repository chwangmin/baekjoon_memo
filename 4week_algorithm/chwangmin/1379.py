# Pass

import sys

input = sys.stdin.readline

num = int(input())

list_room = [list(map(int,input().split())) for _ in range(num)]

list_room.sort(key=lambda x : x[0])

