import sys

re_count = int(sys.stdin.readline())

prime_nums = list()

def prime_list(n):
    for i in range(2,n-1):
        if prime_check(i):
            prime_nums.append(i)

def prime_check(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

prime_list(10000)

for i in range(re_count):
    num = int(sys.stdin.readline())


    for i in range(num // 2, 0, -1):
        if i in prime_nums:
            if num - i in prime_nums:
                print(str(i) + " " + str(num-i))
                break