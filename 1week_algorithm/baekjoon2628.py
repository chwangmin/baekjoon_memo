import sys

x , y = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())

box_x = list()
box_y = list()

box_x.append(x)
box_y.append(y)
box_x.append(0)
box_y.append(0)

for i in range(n):
    choice, dis = map(int,sys.stdin.readline().split())
    if choice:
        box_x.append(dis)
    else:
        box_y.append(dis)

box_x.sort()
box_y.sort()
max_x = 0
max_y = 0
for i in range(1, len(box_x)):
    if box_x[i] - box_x[i-1] > max_x:
        max_x = box_x[i] - box_x[i-1]

for i in range(1, len(box_y)):
    if box_y[i] - box_y[i-1] > max_y:
        max_y = box_y[i] - box_y[i-1]

print(max_x)
print(max_y)
print(max_x * max_y)
