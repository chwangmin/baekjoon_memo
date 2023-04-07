import sys

x = int(sys.stdin.readline())

if 100 >= x > 89:
    print("A")
elif x > 79:
    print("B")
elif x > 69:
    print("C")
elif x > 59:
    print("D")
else:
    print("F")