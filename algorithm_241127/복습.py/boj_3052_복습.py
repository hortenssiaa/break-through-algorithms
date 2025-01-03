x = 10
N = 42
remainder = [0] * N # 42개 (0~41)

for i in range(x):
    num = int(input())
    idx = num % N
    remainder[idx] = 1

print(remainder.count(1))