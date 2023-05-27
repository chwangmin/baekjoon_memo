import sys

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

def back_tracking(cnt,idx):
    if cnt == L:
        vo = 0
        co = 0
        for i in range(L):
            if answer[i] in vowels:
                vo +=1
            else:
                co +=1
        if vo >= 1 and co >=2:
            print("".join(answer))
    for i in range(idx,C):
        answer.append(char_list[i])
        back_tracking(cnt+1,i+1)
        answer.pop()

L, C = map(int,input().split())

char_list = list((input().split()))

char_list.sort()

vowels = ['a','e','i','o','u']

answer = []

back_tracking(0,0)