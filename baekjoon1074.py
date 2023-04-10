import sys

n, y, x = map(int,sys.stdin.readline().split())

x = x + 1
y = y + 1

def z_recursive(n,x,y):
    check = 0
    if n < 1:
        return 0
    if x > 2 ** (n-1) and y > 2 ** (n-1):
        check = 2 ** (2 * (n-1)) * 3
        x = x-2**(n-1)
        y = y-2**(n-1)
    elif x > 2 ** (n-1) and y <= 2 ** (n-1):
        check = 2 ** (2 * (n-1))
        x = x-2**(n-1)
    elif x <= 2 ** (n-1) and y > 2 ** (n-1):
        check = 2 ** (2 * (n-1)) * 2
        y = y-2**(n-1)
    return check + z_recursive(n-1,x,y)

print(int(z_recursive(n,x,y)))
