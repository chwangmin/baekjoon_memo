import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

# print((x // 10 ** 0 % 10) * 10 ** 0)
# print((x // 10 ** 1 % 10) * 10 ** 1)
# print((x // 10 ** 2 % 10) * 10 ** 2)

for i in range(3):
    print((y // (10 ** i) % 10) * x)
print(x*y)