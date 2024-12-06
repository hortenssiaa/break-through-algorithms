N = int(input())
M = int(input())
S = input()

# 해쉬 값을 계산하기 위한 준비물
mod = 1e9 + 7 # 1억 7
po = [0] * 9 # 31의 i승 > 인덱스에 맞게 넣어두기
po[0] = 1
for i in range(1, M):
    po[i] = po[i - 1] * 31 % mod

# Pn
Pn = "I"
for i in range(N): # N == 1; "IOI", N == 2; "IOIOI"
    Pn += "OI"

# Pn의 해쉬 값 계산 - Pn (== "IOI")의 
Pn_hash = 0
for i in range(len(Pn)):
    Pn_hash *= 31
    Pn_hash %= mod

    Pn_hash += ord(Pn[i]) - ord('A') + 1
    Pn_hash %= mod

# S[0:len(Pn)] - S의 첫 S[0, 3(==K)] 까지는 구해야함
S_hash = 0
for i in range(K):
    S_hash *= 31
    S_hash %= mod

    S_hash += ord(S[i]) - ord('A') + 1
    S_hash %= mod

# S의 부분 문자열들의 해쉬 값을 계산 (⭐️여기가 어려웠음 ㅠㅠ)
count = 0
for i in range(0, M - k + 1): # M: S의 길이, K: Pn (== "IOI")의 길이
    if S_hash == Pn_hash:
        count += 1

    # S_hash 갱신
    largest = ord(S[i]) - ord('A') + 1 # 맨 앞(큰) 문자 없애고, 그 다음 S[i+K]의 문자 추가하여, 갱신해야하니깐
    S_hash += mod - largest * po[K - 1] % mod # 매 값마다 mod 나눠주는건 : 무한히 커지는 수를 방지하기 위함
    S_hash %= mod

    S_hash *= 31
    S_hash %= mod

    if i + K < M:
        S_hash += ord(S[i + K]) - ord('A') + 1
        S_hash %= mod

print(count)
    
# Q. 해시 값을 계산할 때, 모듈러 연산(mod)을 사용하는 이유
# A1. 해시 값을 계산할 때, 모듈러 연산(mod)을 사용하는 이유
# A2. 해시 값의 범위를 일정하게 유지하기 위해서
# 해시 값을 계산하는 과정에서 음수가 발생할 수 있는 경우, 이를 방지하기 위해 mod를 더해 양수로 만들어 주는 것입니다. 
# 이렇게 하면 해시 값이 항상 양수가 되어, 해시 테이블이나 다른 자료 구조에서 인덱스로 사용하기에 적합해집니다.
# 예를 들어, 해시 값을 계산할 때 S_hash = (S_hash * base + new_value) % mod와 같은 식을 사용하게 되는데, 
# 이 과정에서 S_hash가 음수가 될 수 있습니다. 
# 따라서 S_hash = (S_hash * base + new_value + mod) % mod와 같이 mod를 더해주면 음수 문제를 해결할 수 있습니다.
# 이러한 방법은 해시 충돌을 줄이고, 해시 값의 범위를 일정하게 유지하는 데 도움을 줍니다. 
# 추가적으로, 이는 해시 함수의 성능을 향상시키고, 해시 테이블의 효율성을 높이는 데 기여합니다.