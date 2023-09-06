"""
모두 나누었을때 가장 큰 수 (max) 을 start로 지정
하나의 값만 나왔을 때 가장 큰 수 (sum) 을 end로 지정
start가 end 값과 같거나 작을 때까지(start가 end 값보다 클때까지)
mid를 (start+end)//2로 지정
입력된 `시간`을 for문으로 하나씩 뽑아서
`합계` 값에 추가하기
만약 `합계` 가 mid보다 크다면 0으로 초기화 후
`카운트` +1 더하기
`시간`을 끝까지 모두 확인한 후
`카운트`가 지정된 값보다 작거나 같으면
    end 를 mid - 1 로 ans 를 mid로
`카운트`가 지정된 값보다 크다면
    start를 mid + 1

틀린부분) total + t > mid를 넘을 경우,
total을 0으로 초기화하고 다음 값에 total + t 만큼 추가해야 한다.
"""

n, m = map(int, input().split())
time = list(map(int, input().split()))

start = max(time)
end = sum(time)

ans = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1

    for t in time:
        if total + t > mid:
            count += 1
            total = 0
        total += t

    if count <= m:
        ans = mid
        end = mid - 1

    else:
        start = mid + 1

print(ans)
