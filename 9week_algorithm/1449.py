import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

num, tape_L = map(int,input().split())

water_hole_list = sorted(list(map(int,input().split())))

answer = 0

tmp_tape = -1

for i in water_hole_list:
    if tmp_tape < i:
        tmp_tape = i + tape_L - 1
        answer +=1

print(answer)