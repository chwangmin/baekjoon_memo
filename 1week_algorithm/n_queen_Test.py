import sys

num = int(sys.stdin.readline())

pos = [0] * num
flag_a = [False] * num
flag_b = [False] * (num*2-1)
flag_c = [False] * (num*2-1)

count = 0

def set(i: int) -> None:
    global count
    for j in range(num):
        if ( not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j+num-1]):
            pos[i] = j
            if i == num-1:
                print(pos)
                put()
                count+=1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+num-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+num-1] = False

def put() -> None:
    for j in range(num):
        for i in range(num):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()

set(0)
print(count)