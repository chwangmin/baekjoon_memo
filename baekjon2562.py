import sys

y = []

for i in range(9):
    x = int(sys.stdin.readline())
    y.append(x)

print(max(y))
print(y.index(max(y))+1)