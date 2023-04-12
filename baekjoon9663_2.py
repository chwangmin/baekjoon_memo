import sys

num = int(sys.stdin.readline())

flag_a = [False] * num
flag_b = [False] * (num*2-1)
flag_c = [False] * (num*2-1)

count = 0

def set(i):
    global count
    
    for j in range(num):
        if (not flag_a[j] and
            not flag_b[i+j] and
            not flag_c[i-j+num-1]):

            if i == num-1:
                count+=1
            
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+num-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+num-1] = False

set(0)
print(count)