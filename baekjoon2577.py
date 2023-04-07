import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = str(A * B * C)
numCheck = list(0 for i in range(10))

for i in result:
    numCheck[int(i)] += 1

for i in range(10):
    print(numCheck[i])
