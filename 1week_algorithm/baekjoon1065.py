import sys

N = int(sys.stdin.readline())

count = 99

if N < 100:
    print(N)
else:
    for i in range(100, N+1):
        a = i // 100
        b = i // 10 % 10
        c = i % 10
        for j in range(-4, 5, 1):
            if a + 2 * j == b + j == c:
                count += 1
    print(count)