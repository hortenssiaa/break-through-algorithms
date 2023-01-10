# 1이 될 때까지 #1

n, k = map(int, input().split()) # n >= k

# 내 풀이
count = 0
while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
        
print(count)


# 책 풀이
count2 = 0
while n >= k: # 25>=3 ... 3>=3 일때 까지 계속 해야하니깐
    while n % k !=0:
        n -= 1
        count2 += 1
    n //= k
    count2 += 1

while n > 1:
    n -= 1
    count2 += 1

print(count2)