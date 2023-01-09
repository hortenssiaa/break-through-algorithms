'''
Q. 큰 수의 법칙
5 8 3
2 4 5 4 6
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

'''
1. 5개 중 가장 큰 수 정렬
2. M(8)개를 더해서 가장 큰 수, 연속 인덱스 K(3) 
'''

data.sort() # [6, 5, 4, 4, 2]
# 6 6 6 5 6 6 6 5

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)