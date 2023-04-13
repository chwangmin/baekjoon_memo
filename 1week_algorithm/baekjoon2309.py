import sys

list_tall = []

for i in range(9):
    list_tall.append(int(sys.stdin.readline()))

list_tall.sort()

sum = 0

list_tall.sort()

for i in list_tall:
    sum+=i

fake1 = 0
fake2 = 0
for i in range(9):
    for j in range(i+1,9):
        if list_tall[i] + list_tall[j] == sum-100:
            fake1 = list_tall[i]
            fake2 = list_tall[j]
            break

list_tall.remove(fake1)
list_tall.remove(fake2)

for i in sorted(list_tall):
    print(i)