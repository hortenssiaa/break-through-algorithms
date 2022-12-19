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