# dynamic programming
# 점화식으로 표현
N = int(input())

a = [0] * (N + 1) # 0~N 까지 

a[1] = 0
for i in range(2, N+1): # N까지
    a[i] = 1 + a[i - 1]
    
    if i % 3 == 0: # 3의 배수
        a[i] = min(a[i], 1 + a[i // 3])

    if i % 2 == 0: # 2의 배수
        a[i] = min(a[i], 1 + a[i // 2])

print(a[N])
