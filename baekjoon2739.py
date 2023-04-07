import sys

x = int(sys.stdin.readline())

for i in range(1, 10):
    print(str(x) + " * " + str(i) + " = " + str(x * i)  )