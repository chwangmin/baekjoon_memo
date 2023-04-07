import sys

num = int(sys.stdin.readline())

for i in range(num):
    score = 0
    check = 1
    answer = sys.stdin.readline()
    for i in answer:
        if i == "O":
            score += check
            check += 1
        else:
            check = 1
    print(score)