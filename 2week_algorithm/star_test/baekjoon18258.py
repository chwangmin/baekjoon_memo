import sys
from collections import deque

input = sys.stdin.readline

num = int(input())

que = deque()

for _ in range(num):
    command = list(map(str,input().split()))
    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    else:
        if not que:
            print(-1)
        else:
            print(que[-1])
