import sys

sentence = list(map(str,sys.stdin.readline().split()))

count = 0
for i in sentence:
    count+=1

print(count)

