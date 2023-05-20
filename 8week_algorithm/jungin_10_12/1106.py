import sys

sys.stdin = open('test.txt', 'r')

input = sys.stdin.readline

people_num, city_num = map(int,input().split())

answer_list = [[float('inf')] * (people_num+1) for _ in range(city_num+1)]

for _ in range(city_num):
    x, y = map(int,input().split())
    for i in range(1,people_num+1):
        answer_list[i]