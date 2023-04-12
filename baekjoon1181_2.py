import sys

num = int(sys.stdin.readline())

all = []

for i in range(num):
    all.append(sys.stdin.readline().strip())

all = set(all)
all = list(all)

all.sort()
all.sort(key = len)

for i in all:
    print(i)