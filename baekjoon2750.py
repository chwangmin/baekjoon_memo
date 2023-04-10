import sys

num = int(sys.stdin.readline())

list_sort = []

for i in range(num):
    list_sort.append(int(sys.stdin.readline()))

for i in sorted(list_sort):
    print(i)