import sys

num = int(sys.stdin.readline())

list_sort = [0] * 10001

for i in range(num):
    list_sort[int(sys.stdin.readline())] += 1

for i in range(10001):
    if list_sort[i] > 0:
        while list_sort[i] > 0:
            list_sort[i] -=1
            print(i)