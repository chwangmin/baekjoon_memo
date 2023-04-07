import sys

num = int(sys.stdin.readline())

for i in range(num):
    x = list(map(int,sys.stdin.readline().split()))
    x.pop(0)
    avg = sum(x) / len(x)
    count = 0
    for j in x:
        if j > avg:
            count += 1
    print(f'{count / len(x) * 100:.3f}%')
    print(f'1')

