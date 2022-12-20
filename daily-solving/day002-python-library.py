'''
* 코테를 위한 라이브러리 6개
1. 내장함수
   - 기본 입출력 기능 ~ 정렬기능 포함.
   - print(), input(), sorted()
   - 프로그램 작성시, 필수적 기능 포함

2. itertools
   - 순열, 조합

3. heapq
   - 힙, 우선순위 큐

4. bisect
   - 이진 탐색

5. collections
   - deque, counter 등 자료구조 포함

6. math
   - 수학적 기능
   - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, pi 상수 등
'''

# 1. 내장 함수
# sum
result = sum([1, 2, 3, 4, 5])
print(result)

# min
result = min([7, 3, 5, 2]) # 2
result = min(7, 3, 5, 2) # 2
print(result)

# max
result = max([7, 3, 5, 2])
print(result)

# eval : 문자열 형식의 수학 수식 계산
result = eval("(3+5)*7") # 56
print(result)

# sorted
result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

# key 속성으로 정렬 기준 명시할 수 있다.
# 원소를 튜플의 두번째 원소(나이)를 기준으로 내림차순 정렬하기
result = sorted([('김가나', 43), ('박다라', 20), ('홍마바', 32)], key= lambda x: x[1], reverse=True)
print(result) # [('김가나', 43), ('홍마바', 32), ('박다라', 20)]

# iterable 객체의 기본함수 sort()
# 굳이 sorted() 사용안해도 됨
data = [9, 1, 8, 5, 4]
data.sort()
print(data) # [1, 4, 5, 8, 9]






# 2. itertools
'''
- permutations (순열)
: list와 같은 iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우

- combinations (조합)
: list와 같은 iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우

- product (중복 순열)
: r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (원소 중복)

- combination_with_replacement (중복 조합)
: r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (원소 중복)
'''
# permutations (순열) - 순서 O!
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations (조합) - 순서 X
from itertools import combinations
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

result2 = list(combinations(data, 3))
print(result2) # [('A', 'B', 'C')]

# product (중복 순열) - 순서 O
from itertools import product
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

result2 = list(product(data, repeat=3))
print(result2) # [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'A', 'C'), ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'), ('C', 'A', 'A'), ('C', 'A', 'B'), ('C', 'A', 'C'), ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'), ('C', 'C', 'A'), ('C', 'C', 'B'), ('C', 'C', 'C')]

result3 = list(product(data, repeat=1))
print(result3) # [('A',), ('B',), ('C',)]

# combine_with_replacement (중복 조합) - 순서 X
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]