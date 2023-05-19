import sys

#sys.stdin = open('test.txt', 'r')

input = sys.stdin.readline

room_name = list(map(int,input().rstrip()))

answer_list = [0] * 10

for room_num in room_name:
    answer_list[room_num] += 1

answer=max(answer_list)

if answer_list.index(answer) == 9 or answer_list.index(answer) == 6:
    answer = answer_list[6] + answer_list[9]
    if answer % 2 == 0:
        answer //= 2
        answer_list[6] = answer
        answer_list[9] = answer
    else:
        answer //=2
        answer+=1
        answer_list[6] = answer
        answer_list[9] = answer
answer = max(answer_list)

print(answer)