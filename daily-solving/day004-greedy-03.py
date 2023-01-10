# 숫자 카드 게임

n, m = map(int, input().split())

result = 0

# 내 방법
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    if data[0] > result:
        result = data[0]

print(result)

# 풀이
result2 = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result2 = max(result2, min_value)

print(result2)