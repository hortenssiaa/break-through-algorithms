# my code
# n 으로 나눈 나머지: 0 ~ n-1
# 0~n-1 배열 만들고
# 나머지 나올때 마다 해당　index 값 + 1
# 1 이상인 인덱스 갯수 구하기

check = [0] * 42

for i in range(10) :
  n = int(input())
  check[n % 42] += 1

result = 0
for i in range(42) :
  if check[i] >= 1 :
    result += 1

print(result)


# tutor code
check = [0] * 42

for i in range(10) :
  n = int(input())
  check[n % 42] = 1

sum = 0
for i in range(42) :
  sum += check[i]

print(sum)