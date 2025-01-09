N, M = list(map(int, input().split()))
lecture = list(map(int, input().split()))

left = max(lecture) # 강의 중 최대 길이
right = sum(lecture)

answer = -1
# 이분탐색 ⭐️⭐️⭐️
while left <= right:
    mid = (left + right) // 2

    blueray = 1
    remain = mid
    for i in range(N):
        if lecture[i] > remain:
            blueray += 1
            remain = mid

        remain -= lecture[i]

    if blueray <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer) # 바로 answer이 답인 이유: 이분탐색의 결과이기 때문