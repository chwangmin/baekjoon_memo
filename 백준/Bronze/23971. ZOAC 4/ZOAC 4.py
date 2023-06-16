import sys

input = sys.stdin.readline

H,W,N,M = map(int,input().split())

answer_x = (H-1) // (N+1) + 1
answer_y = (W-1) // (M+1) + 1

print(answer_x * answer_y)