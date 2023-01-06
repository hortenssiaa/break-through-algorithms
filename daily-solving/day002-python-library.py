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





# 3. heapq
'''
- heap 기능을 위해 라이브러리 제공
- 다익스트라 최단경로 알고리즘, 우선순위 큐 기능 구현할때 사용
- 파이썬 힙은, 최소 힙
  > 단순히 원소를 힙에 전부 넣었다 빼는 것만으로 O(NlogN)에 오름차순 정렬 완료
- heapq.heappush() : 힙에 원소 삽입
- heapq.heappop() : 힙에 원소 꺼낼때 
'''

# 힙 정렬을 heapq로 구현하기
import heapq
def heapsort(iterable):
    h = []
    result = []

    # 모든 원소 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] O(NlogN)


# 내림차순 힙 정렬 구현
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소 차례대로 꺼내 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  O(NlogN)




# 4. bisect
'''
- 이진탐색을 쉽게 구현하는 라이브러리
- 정렬된 배열에서 특정원소 찾아야 할때 매우 효과적
- 핵심함수: bisect_left(), bisect_right()
   -> 시간복잡도: O(logN)
- bisect_left(a, x) : 
   - 리스트 a, 삽입할 숫자 x
   - 정렬된 순서를 유지하면서 리스트 a에 x 를 삽입할때, 가장 왼쪽에 있는 인덱스 값!!을 찾는 메서드
- bisect_right(a, x) :
   - 리스트 a, 삽입할 숫자 x
   - 정렬된 순서를 유지하면서 리스트 a에 x 를 삽입할때, 가장 오른쪽에 있는 인덱스 값!!을 찾는 메서드
- 예) [1, 2, 4, 4, 8]
      bisect_left(a, 4) : 2
         [1, 2, (여기), 4, 4, 8]
      bisect_right(a, 4) : 4
         [1, 2, 4, 4, (여기), 8]
'''
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


# *** bisect_left(), bisect_right() 로, 특정 범위에 속하는 원소의 개수를 구할 수 있음
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 7, 7, 7, 8, 9]
print(count_by_range(a, 3, 7))

# *** bisect_left(), bisect_right() 로, 특정 원소의 개수를 구할 수 있음
def count_the_number(a, x):
    right_index = bisect_right(a, x)
    left_index = bisect_left(a, x)
    return right_index - left_index

print(count_the_number(a, 3))
print(count_the_number(a, 4))
print(count_the_number(a, 7))



# collections
'''
- 코테에서 유용하게 사용되는 클래스: deque, Counter
- duque: 큐 자료구조 구현
        - 가장 앞/뒤 원소 추가/제거 : O(1)
            - 첫 번째 원소 제거 : popleft()
            - 마지막 원소 제가 : pop()
            - 첫 번째 원소 삽입 : appendleft(x)
            - 마지막 원소 삽입 : append(x)
        - 스택, 큐 기능 포함
- list: append(), pop() 이 O(1)으로 가능하지만, '맨 뒤 원소'를 기준
        가장 앞 원소 추가/제거 : O(N)
'''

# collections - dequeue
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # list 자료형으로 변환


# collections - Ciounter
# 등장 횟수를 세는 기능
'''
리스트와 같은 iterable 객체 내에, 원소가 몇번씩 등장했는지 알 수 있음
'''

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['Blue'])
print(counter['green'])
print(dict(counter))