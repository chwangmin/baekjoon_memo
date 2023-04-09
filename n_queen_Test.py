import sys
input = sys.stdin.readline

def bt(row):
    global ans
    
    # escape
    if row == n:
        ans += 1
        return

    for j in range(n if row else n//2):
        print(n)
        if not col[j] and not d1[row-j] and not d2[row+j]:
            col[j] = True
            d1[row-j] = True
            d2[row+j] = True

            bt(row+1)

            col[j] = False
            d1[row-j] = False
            d2[row+j] = False

n = int(input())
ans = 0

col = [False for _ in range(n)]
# right-down
d1 = [False for _ in range(n*2)]
# left-down
d2 = [False for _ in range(n*2)]

# odd n: half*2 + mid
if n % 2:
    bt(0)
    ans *= 2
    # mid
    j = n//2
    # row == 1
    col[j] = d1[-j] = d2[j] = True
    bt(1)

# even n: half*2
else:
    bt(0)
    ans *= 2

print(ans)