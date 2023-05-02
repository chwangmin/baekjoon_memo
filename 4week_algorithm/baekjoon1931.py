import sys

input = sys.stdin.readline

num = int(input())

list_meeting = []

for i in range(num):
    list_meeting.append(list(map(int, input().split())))

list_meeting.sort(key=lambda x : (x[1],x[0]))

end = list_meeting[0][1]
answer = 1

for i in range(1,num):
    if end <= list_meeting[i][0]:
        end = list_meeting[i][1]
        answer +=1

print(answer)