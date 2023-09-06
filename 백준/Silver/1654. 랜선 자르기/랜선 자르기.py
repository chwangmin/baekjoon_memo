"""
이분 탐색 공식활용
start = max(lans) // n로 지정
end = sum(lans) // n

만약 count 가 n 보다 크다면
"""

k, n = map(int, input().split())
lans = list()

for _ in range(k):
    lans.append(int(input()))

start = max(lans) // n or 1
end = sum(lans) // n

ans = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for l in lans:
        count += l // mid

    if count >= n:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)
