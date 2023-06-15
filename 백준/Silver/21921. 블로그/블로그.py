import sys

#sys.stdin = open('test.txt', 'r')

input = sys.stdin.readline

N, X = map(int,input().split())

visit = list(map(int,input().split()))

answer = sum(visit[:X])

answer_cnt = 1

tmp = answer

for i in range(X,N):
    tmp += visit[i] - visit[i-X]
    if answer < tmp:
        answer = tmp
        answer_cnt = 1
    elif answer == tmp:
        answer_cnt += 1

if answer == 0:
    print("SAD")
    exit()

print(answer)
print(answer_cnt)