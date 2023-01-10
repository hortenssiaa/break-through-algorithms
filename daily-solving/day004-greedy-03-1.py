# 숫자 카드 게임 #2
# 풀이2 - 2중 반목문 사용하기

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)