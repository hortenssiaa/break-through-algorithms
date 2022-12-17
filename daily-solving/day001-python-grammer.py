# 1. 자료형
# 1.1 실수형 - e
"""
* 지수 표현 방식
>> 유효숫자e^지수 == 유효숫자*10^지수
>> 1,000,000,000 == 1e9 == 10억
>> 자릿수가 커서, 헷갈리는 경우 많기때문!
"""

a = 1e9
print(a) # 1000000000.0

a = 75.25e1
print(a) # 752.5



# 1.2 실수형 - 소수점 값 비교
"""
실수형 데이터 비교할 때 : 소수점 다섯번째 자리에서 반올림한 결과가 같으면 정답! == round(a, 4)
"""
a = 0.3 + 0.6
print(a) # 0.8999999999999999

if a == 0.9: # False
    print(True)
else:
    print(False)

# round(a, 4)
if round(a, 4) == 0.9: # a 를 소숫점 5번째 자리에서 반올림
    print(True)
else:
    print(False)


# 1.3 수 자료형의 연산
a = 7
b = 3

# 나누기
print(a/b) # 2.3333333333333335

# 나머지
print(a%b)

# 몫
print(a//b)









# 2. List
# 2.1 list comprehension

'''0부터 19까지의 수 중에서 홀수만 포함하는 리스트'''
array = [i for i in range(20) if i % 2 == 1]
print(array) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

'''1부터 9까지의 수의 제곱 값을 포함하는 리스트'''
array = [i*i for i in range(1, 10)]
print(array) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

'''n X m 크기의 2차원 리스트 초기화'''
'''
Usage of underbar _ ?
> 값 상관없이, 반복 횟수만 중요할 때 사용! 
'''
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



# 2.2 list function
# 변수명.count(특정값) : O(N)
a = [1, 4, 3, 1]
print(a.count(1)) # 2

# 변수명.remove(특정값) : O(N)
a.remove(3)
print(a) # [1, 4, 1]



'''함수 쓰지않고, remove_set 리스트에 포함안된 값만 저장하기
>> 시간복잡도 고려한 풀이 '''
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result) # [1, 2, 4]








# 3. 문자열
a = "ABCDEF"
print(a[2:4]) # CD






# 4. 튜플
'''
- 튜플은 한 번 선언된 값을 변경할 수 없다.
- ( ) 이용
- 그래프 알고리즘 구현시 많이 사용
  예) 다익스트라 최단경로 알고리즘에서, 내부에서 우선순위 큐 이용하는데, 이때 큐는 튜플로 작성됨 
      > (비용, 노드번호) 형태로 묶어서 관리
- 튜플로, 변경하면 안되는 값 변경되고있지 않은지 체크 가능
'''
a = (1, 2, 3, 4)
print(a) # (1, 2, 3, 4)

# a[2] = 7 # error






# 5. Dictionary 사전
'''
데이터의 검색 / 수정 : O(N)
'''

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("사과 yes!")





# 6. Set 집합
'''
특정원소 존재유무 : O(N)
'''

# 6.1 집합 초기화 방법
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)


# 6.2 집합 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b) # {1, 2, 3, 4, 5, 6, 7}

# 교집합
print(a & b) # {3, 4, 5}

# 차집합
print((a - b)) # {1, 2}



'''
-------|-------|-------|-------
  리스트 |  튜플  |  집합  |  사전
-------|-------|-------|-------
  [ ]  |  ( )  |  {  } | [k,v]
-------|-------|-------|-------|
         in , not in
-------------------------------
'''




# 7. 조건문
# 7.1 pass
'''조건문 값이 참이라도, 아무것도 처리하고 싶지 않을때 pass 이용'''
score = 82
if score >= 80:
    pass # 나중에 작성할 코드
else:
    print("성적이 낮아요")


# 7.2 conditional expression 조건부 표현식
'''변수 = true일때값(1) if조건문(2) else(3) false일때값(4)'''
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 7.2.1 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할때
a = [1, 2, 3, 4, 5]
remove = [3, 5]

result = [i for i in a if i not in remove]
print(result) # [1, 2, 4]


# 7.3 수학 부등식 그대로 사용가능!
x = 15
if x > 0 and x < 20:
    print(f"0 < {x} < 20")

if 0 < x < 20:
    print(f"0 < {x} < 20")





# 8. 반복문
# 8.1 중첩 반복문
'''
- 플로이드 워셜 알고리즘
- 다이나믹 프로그래밍 등에서 많이 사용된다.
'''
scores = [90, 85, 77, 65, 97]
cheating_list = [2, 4]

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")







# 9. 함수
# 문제 푸는 코드를 함수화하면, 매우 효과적으로 풀 수 있다.

# 9.1 global
# 함수 안에서, 함수 밖의 변수 데이터를 변경해야하는 경우
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) # 10


# 9.2 람다 표현식
# python의 정렬 라이브러리를 사용할때, 정렬 기준 (key)를 설정할 때에도 자주 사용된다.
def add(a, b):
    return a+b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print( (lambda a, b: a+b)(3, 7) )












# 10. 입출력
# 10.1 입력을 위한 전혁적인 소스코드
''' list(map(int, input().split())) '''

# ex 1)
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)
'''
input
5
65 90 75 34 99

result
[99, 90, 75, 65, 34]
'''


# ex 2)
# n, m, k를 공ㅇ백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)




# 10.2 더 빠른 코드 - sys.stdin.readline()
'''
- sys 라이브러리를 사용할때는, 한 줄 입력을 받고 나서 rstrip() 을 꼭 호출해야 한다.
- sys.stdin.readline() 까지만 작성하면, 입력 후 엔터가 줄바꿈 기호로 입력된다. 
   > 이때 이 공백 문자를 제거하려면, rstrip() 함수를 사용해야한다. 
'''
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)



# 10.3 변수를 문자열로 출력
answer = 7

print("정답은 " + answer + " 입니다.") # error
print("정답은 " + str(answer) + "입니다.") # 정답은 7입니다.
print("정답은", answer, "입니다.") # 정답은 7 입니다. (띄어쓰기 포함! )
print(f"정답은 {answer}입니다.") # 정답은 7입니다.