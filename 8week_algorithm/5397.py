import sys, collections

sys.stdin = open('test.txt','r')

input = sys.stdin.readline

num = int(input())

for _ in range(num):
    char_list = input().rstrip()
    tmp_queue = collections.deque()
    answer = []
    for i in char_list:
        if i == '<':
            if answer:
                tmp_queue.append(answer.pop())
        elif i == '>':
            if tmp_queue:
                answer.append(tmp_queue.pop())
        elif i == '-':
            if answer:
                answer.pop()
        else:
            answer.append(i)
    for i in range(len(tmp_queue)):
        answer.append(tmp_queue.pop())
    print(*answer, sep='')
