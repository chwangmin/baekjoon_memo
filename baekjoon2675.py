import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = map(str,sys.stdin.readline().split())
    for j in b:
        for i in range(int(a)):
            print(j,end='')
    print()